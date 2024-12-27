from abc import ABC, abstractmethod
from typing import Any


from Carta import Carta


class Porta(Carta, ABC):
    @abstractmethod
    def acao(self, parametro: Any) -> None:
        pass
