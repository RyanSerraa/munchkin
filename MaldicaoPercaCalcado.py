from Jogador import Jogador
from Maldicao import Maldicao


class MaldicaoPercaCalcado(Maldicao):
    def acao(self, jogador: Jogador) -> None:
        print(f"O jogador {jogador.get_nome()} perdeu um calçado.")
