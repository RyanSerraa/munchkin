from Partida import Partida

class Jogo:
    def __init__(self):
        self.__partida_atual: Partida = Partida()

    def iniciar_jogo(self) -> None:
        raise NotImplementedError()

    def finalizar_jogo(self) -> None:
        raise NotImplementedError()