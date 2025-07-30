from ..loader import monkeypatch_schema
from ..skeleton import Canvas, AnnotationBody


class SetHwd:
    def set_hwd(self, height=None, width=None, duration=None):
        """Set the height, width, and duration properties allowing nulls.

        Args:
            height (int): The height of the resource or the canvas
            width (int): The width of the resource or the canvas
            duration (float): The duration of the resource
        """
        if not (duration or height or width):
            raise TypeError("At least one of height, width, or duration must be set")
        if height and not width:
            raise TypeError("width must be set if height is set")
        if width and not height:
            raise TypeError("height must be set if width is set")
        self.height = height
        self.width = width
        self.duration = duration


monkeypatch_schema([Canvas, AnnotationBody], [SetHwd])
