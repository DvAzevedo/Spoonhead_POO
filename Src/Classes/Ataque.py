from abc import ABC, abstractmethod
from Classes.Animacao import *
from Classes.Personagem import *
from Classes.Chalice.listasDeImagens import CollideSmoke

class Ataque(ABC, Image):
    QTD_IMAGENS_SMOKE = 8
    def __init__(self, x: int, y: int, alvo: Personagem, animacao: Animacao, dano: int) -> None:
        self._x = x
        self._y = y
        self._alvo = alvo
        self._animacao = animacao
        self._animacaoSmoke = Animacao(Ataque.QTD_IMAGENS_SMOKE, CollideSmoke, 1)
        self._dano = dano
        pass
    
    @property
    def posX(self) -> int:
        return self._x
    
    @posX.setter
    def posX(self, x: int) -> None:
        self._x = x
        pass
    
    @property
    def posY(self) -> int:
        return self._y
    
    @posY.setter
    def posY(self, y: int) -> None:
        self._y = y
        pass
    
    @property
    def alvo(self) -> Personagem:
        return self._alvo
    
    @alvo.setter
    def alvo(self, alvo: Personagem) -> None:
        self._alvo = alvo
        pass
    
    @property
    def animacao(self) -> Animacao:
        return self._animacao
    
    @animacao.setter
    def animacao(self, animacao: Animacao) -> None:
        self._animacao = animacao
        pass
    
    @property
    def dano(self) -> int:
        return self._dano
    
    @dano.setter
    def dano(self, dano: int) -> None:
        self._dano = dano
        pass
    
    @abstractmethod
    def atualiza_coordenadas(self):
        pass
    
    @abstractmethod
    def causa_dano(self):
        pass
    
    def colide_com_alvo(self, alvo: Personagem) -> bool:
        if self._collides_with(alvo.hitbox):
            return True
        return False
    
    def fora_da_tela(self) -> bool:
        if self.posX < -20 or self.posX > 840 or self.posY < 0 or self.posY > 800:
            return True
        return False