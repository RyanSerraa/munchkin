
class Verificador:
    @staticmethod
    def verificar_nivel(jogadores: List[Jogador]) -> bool:
        for jogador in jogadores:
            if jogador.get_nivel() == 10:
                return True
        return False
    @staticmethod
    def exibir_nivel(jogadores: List[Jogador]) -> None:
        for jogador in jogadores:
            print(jogadores.getNivel())