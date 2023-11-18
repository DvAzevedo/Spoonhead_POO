from tupy import *
from abc import ABC, abstractmethod

class Personagem(Image, ABC):
    def __init__(self, x: int, y: int, vida: int) -> None:
        self._x = x
        self._y = y
        self._vida = vida
        pass
    
    @property
    def posX(self) -> int:
        return self._x
    
    @posX.setter
    def posX(self, x) -> None:
        self._x = x
        pass
    
    @property
    def posY(self) -> int:
        return self._y
    
    @posY.setter
    def posY(self, y) -> None:
        self._y = y
        pass
    
    @property
    def vida(self) -> int:
        return self._vida
    
    @vida.setter
    def vida(self, vida) -> None:
        self._vida = vida
        pass
    
    def decrementa_vida(self, dano) -> None:
        self.vida -= dano
        pass