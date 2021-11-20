from ..skeleton import Id
from ..loader import monkeypatch_schema

class Ident:
    def __str__(self):
        return str(self.__root__)


monkeypatch_schema(Id, Ident)
