from Jogador import Jogador
from Turno import Turno


# Status de partida: 0 = Não iniciado, 1 = Iniciado, 2 = Encerrado
class Partida:
    def __init__(self):
        self.__jogadores: list[Jogador] = []
        self.__turno: Turno = Turno()
        self.__status: int = 0
        self.__max_jogadores: int = 4


    def iniciar_partida(self):
        self.__status = 1


    def finalizar_partida(self):
        self.__status = 2


    def adicionar_jogador(self, jogador: Jogador):
        if self.__status == 0:
            if len(self.__jogadores) < self.__max_jogadores:
                self.__jogadores.append(jogador)
                print(f"Jogador {jogador.get_nome()} adicionado")
            else:
                print(f"Limite de {self.__max_jogadores} jogadores atingido")
        else:
            print("Só é possível adicionar jogadores antes de iniciar uma partida")


    def marcador (self):
        raise NotImplementedError()

    def distribuir_cartas (self):
        raise NotImplementedError()

    def criar_cartas (self):
        raise NotImplementedError()


    # Função que verifica o nível utilizando a classe Verificador
    def verificar_nivel(self, nome: str):
        jogador_encontrado = next((j for j in self.__jogadores if j.get_nome() == nome), None)
        if jogador_encontrado:
            print(f"Nível do jogador {jogador_encontrado.get_nome()}: {self.__turno.verificar_nivel(jogador_encontrado)}")
        else:
            print(f"Jogador com o nome '{nome}' não encontrado.")


    # Função que verifica o nível o nível do jogador diretamente
    def verificar_nivel_2(self, nome: str):
        jogador_encontrado = next((j for j in self.__jogadores if j.get_nome() == nome), None)
        if jogador_encontrado:
            print(f"Nível do jogador {jogador_encontrado.get_nome()}: {jogador_encontrado.get_nivel()}")
        else:
            print(f"Jogador com o nome '{nome}' não encontrado.")

