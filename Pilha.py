from Carta import Carta
from abc import ABC, abstractmethod
from typing import Any

class Pilha(ABC):
  
  @abstractmethod
  def pilha_compra(self, carta: Any) -> Any:
    pass

  @abstractmethod
  def pilha_descarte(self, carta: Any) -> Any:
    pass

  @abstractmethod
  def pilha_mesa(self, carta: Any) -> Any:
    pass

  @abstractmethod
  def sortear(self) -> Any:
    pass