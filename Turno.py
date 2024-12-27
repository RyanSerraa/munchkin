from Verificador import Verificador
from Jogador import Jogador


class Turno:
    # Declaração de variaveis
    def __init__(self):
        self.__verificador: Verificador = Verificador()


    def verificar_nivel(self, jogador: Jogador) -> int:
        return self.__verificador.verificar_nivel(jogador)

    def caridade(self):
        return None

    def abrirPorta(self):
        return None

    def SaquearSala(self):
        return None

    def ProcurarEncrenca(self):
        return None

    def passarVez(self):
        return None
