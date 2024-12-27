from abc import ABC, abstractmethod
from typing import Any


class Carta(ABC):
    def __init__(self, nome: str, imagem: str) -> None:
        self.__nome = nome
        self.__imagem = imagem

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_imagem(self):
        return self.__imagem

    def set_imagem(self, imagem: str):
        self.__imagem = imagem

    @abstractmethod
    def acao(self, parametro: Any) -> None:
        pass
