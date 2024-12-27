from abc import ABC, abstractmethod
from typing import Any


class Carta(ABC):
    def __init__(self, nome: str, image: str) -> None:
        self.nome = nome
        self.image = image

    @abstractmethod
    def acao(self, parametro: Any) -> None:
        pass
