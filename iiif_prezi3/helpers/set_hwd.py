from ..loader import monkeypatch_schema
from ..skeleton import Canvas, ResourceItem


class SetHwd:
    def set_hwd(self, height, width, duration):
        """Set the height, width, and duration properties allowing nulls.

        Args:
            height (int): The height of the resource or the canvas
            width (int): The width of the resource or the canvas
            duration (float): The duration of the resource

        Returns:
            None
        """
        if duration is None and height is None and width is None:
            raise TypeError("At least one of height, width, or duration must be set")
        if height is not None and width is None:
            raise TypeError("width must be set if height is set")
        if width is not None and height is None:
            raise TypeError("height must be set if width is set")
        self.height = height
        self.width = width
        self.duration = duration
        return None


monkeypatch_schema([Canvas, ResourceItem], [SetHwd])
