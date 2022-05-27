from ..config import configs
from ..loader import monkeypatch_schema
from ..skeleton import (Annotation, AnnotationPage, Canvas, Collection,
                        Manifest, Range, ResourceItem)


class AddLabel:

    def add_label(self, value, language=None):
        if not self.label:
            if not language:
                self.label = value
            else:
                if type(value) != list:
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
                if type(value) != list:
                    value = [value]
                curr[language] = value
            self.label = curr


monkeypatch_schema([Collection, Manifest, Canvas, Range, Annotation, AnnotationPage, ResourceItem], AddLabel)
