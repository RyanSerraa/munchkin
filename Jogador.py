import pygame


class Jogador:
    # Declaração de variaveis
    def __init__(self):
        self.__nivel: int = 1
        self.__forca: int = 1
        self.__sexo: str = ""

    # Getter e Setter para 'nivel'
    def get_nivel(self) -> int:
        return self.__nivel

    def set_nivel(self, nivel: int) -> None:
        if nivel > 0:  # Validação
            self.__nivel = nivel
        else:
            raise ValueError("O nível deve ser maior que zero.")

    # Getter e Setter para 'forca'
    def get_forca(self) -> int:
        return self.__forca

    def set_forca(self, forca: int) -> None:
        if forca > 0:  # Validação
            self.__forca = forca
        else:
            raise ValueError("A força deve ser maior que zero.")

    # Getter e Setter para 'sexo'
    def get_sexo(self) -> str:
        return self.__sexo

    def set_sexo(self, sexo: str) -> None:
        self.__sexo = sexo
