import mimetypes
import os

from PIL import Image

from ..loader import monkeypatch_schema
from ..skeleton import Canvas


class SetHeightWidthDurationFileHelper:
    def set_hwd_from_file(self, file_path_or_object):
        """Introspect a file and set the height, width, and duration properties.

        Args:
            file_path_or_object (Union[str, fp]): the file path or file object to introspect
        """
        if isinstance(file_path_or_object, str) or isinstance(file_path_or_object, os.PathLike):
            filetype, _ = mimetypes.guess_type(file_path_or_object)
            if not filetype.startswith("image/"):
                raise NotImplementedError

        tmp_image = Image.open(file_path_or_object)
        w, h = tmp_image.size
        self.set_hwd(h, w, None)
        tmp_image.close()


monkeypatch_schema(Canvas, SetHeightWidthDurationFileHelper)
