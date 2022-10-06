import mimetypes

from PIL import Image

from ..loader import monkeypatch_schema
from ..skeleton import Canvas


class SetHeightWidthDurationFileHelper:
    """Introspect a file and set the height, width, and duration properties.

    Args:
        file_path_or_object (filepath or fileobject): the file path or file object to introspect

    Returns:
        None
    """

    def set_hwd_from_file(self, file_path_or_object):
        if isinstance(file_path_or_object, str):
            filetype, _ = mimetypes.guess_type(file_path_or_object)
            if not filetype.startswith("image/"):
                raise NotImplementedError

        tmp_image = Image.open(file_path_or_object)
        w, h = tmp_image.size
        self.set_hwd(h, w, None)
        tmp_image.close()


monkeypatch_schema(Canvas, SetHeightWidthDurationFileHelper)
