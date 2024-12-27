from abc import ABC, abstractmethod
from typing import Any


import Carta


class Tesouro(Carta, ABC):
    @abstractmethod
    def acao(self, parametro: Any) -> None:
        pass
