from Jogador import Jogador
from Maldicao import Maldicao


class MaldicaoClasse(Maldicao):
    def acao(self, jogador: Jogador) -> None:
        print(f"A classe do jogador {jogador.get_nome()} foi afetada.")
