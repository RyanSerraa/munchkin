from abc import ABC, abstractmethod
from typing import Any

from Porta import Porta


class Maldicao(Porta, ABC):
    @abstractmethod
    def acao(self, parametro: Any) -> None:
        pass
