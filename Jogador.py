
class Jogador:
    # Declaração de variaveis
    def __init__(self):
        self.__nome: str = "Sem nome"
        self.__nivel: int = 1
        self.__forca: int = 1
        self.__sexo: str = ""
     # Getter e Setter para 'nivel'
    def get_nivel(self) -> int:
        return self.__nivel

    def set_nivel(self, nivel: int):
        if nivel > 0:  # Validação
            self.__nivel = nivel
        else:
            raise ValueError("O nível deve ser maior que zero.")

    # Getter e Setter para 'forca'
    def get_forca(self) -> int:
        return self.__forca

    def set_forca(self, forca: int):
        if forca > 0:  # Validação
            self.__forca = forca
        else:
            raise ValueError("A força deve ser maior que zero.")

    # Getter e Setter para 'sexo'
    def get_sexo(self) -> str:
        return self.__sexo

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_sexo(self, sexo: str):
        self.__sexo = sexo
