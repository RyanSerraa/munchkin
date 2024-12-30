from Jogador import Jogador
from Maldicao import Maldicao


class MaldicaoRaca(Maldicao):
    def acao(self, jogador: Jogador) -> None:
        print(f"A raça do jogador {jogador.get_nome()} foi afetada.")
