from Jogador import Jogador
from Maldicao import Maldicao


class MaldicaoPercaArmadura(Maldicao):
    def acao(self, jogador: Jogador) -> None:
        print(f"O jogador {jogador.get_nome()} perdeu uma armadura.")
