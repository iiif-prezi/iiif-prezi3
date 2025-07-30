from ..config import configs
from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationPage, Canvas, Collection,
                        Manifest, Range, AnnotationBody)


class AddLabel:

    def add_label(self, value, language=None):
        """Adds a label to an existing resource.

        Args:
            value (Union[str, list]): The label or labels to be added
            language (str): An optional language for the labels. If not provided it will default using the AutoLang configuration.
        """
        if not self.label:
            if not language:
                self.label = value
            else:
                if not isinstance(value, list):
                    value = [value]
                self.label = {language: value}
        else:
            # fetch as dict not LngString
            curr = self.label
            if not language:
                language = configs['helpers.auto_fields.AutoLang'].auto_lang
            if language in curr:
                curr[language].append(value)
            else:
                if not isinstance(value, list):
                    value = [value]
                curr[language] = value
            self.label = curr


monkeypatch_schema([Collection, Manifest, Canvas, Range, Annotation, AnnotationPage, AnnotationBody], AddLabel)
