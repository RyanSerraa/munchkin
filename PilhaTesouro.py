from Pilha import Pilha
from Tesouro import Tesouro
from typing import List

class PilhaTesouro(Pilha):

  def __init__(self):
    self.__pilha_compra: List[Tesouro] = []
    self.__pilha_descarte: List[Tesouro] = []
    self.__pilha_mesa: List[Tesouro] = []


  def pilha_compra(self, carta: Tesouro) -> Tesouro:
    pass

  def pilha_descarte(self, carta: Tesouro) -> Tesouro:
    pass

  def pilha_mesa(self, carta: Tesouro) -> Tesouro:
    pass

  def sortear(self) -> Tesouro:
    pass
  
  def verificar_tamanho(self, tesouro: Tesouro) -> Tesouro:
    pass