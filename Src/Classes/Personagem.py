from tupy import Image
from abc import ABC, abstractmethod
from Classes.Hitbox import HitBox

class Personagem(Image, ABC):
    def __init__(self, x: int, y: int, vida: int, hitbox: HitBox) -> None:
        self._x = x
        self._y = y
        self._vida = vida
        self._hitbox = hitbox
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
    
    @property
    def hitbox(self) -> HitBox:
        return self._hitbox
    
    @hitbox.setter
    def hitbox(self, hitbox: HitBox) -> None:
        self._hitbox = hitbox
        pass
    
    @abstractmethod
    def ataca(self):
        pass
    
    @abstractmethod
    def movimenta(self):
        pass
    
    def decrementa_vida(self) -> None:
        self.vida -= 1
        pass
    
    def sofre_dano(self, dano) -> None:
        self.vida -= dano
        pass
