class Verificador:
    def __init__(self):
        pass

    def verificar_nivel(self, jogador) -> int:
        return jogador.get_nivel()

    # Ao meu ver, o bloco abaixo é a forma correta de verificar o nível, porém não é possivel pois o Verificador não tem acesso a classe Jogador de acordo com o diagrama
    """
    def verificar_nivel(self, jogador: Jogador) -> int:
        return jogador.get_nivel()
    """
