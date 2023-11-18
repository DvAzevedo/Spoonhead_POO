from tupy import Image
from abc import ABC, abstractmethod
from Classes.Animacao import Animacao
from Classes.Personagem import Personagem

class Ataque(ABC, Image):
    def __init__(self, x: int, y: int, imagens: list, animacao: Animacao, alvo: Personagem, dano: int) -> None:
        self._x = x
        self._y = y
        self._listaDeImagens = imagens
        self._animacao = animacao
        self._alvo = alvo
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
    def listaDeImagens(self) -> list:
        return self._listaDeImagens
    
    @listaDeImagens.setter
    def listaDeImagens(self, imagens: list) -> None:
        self._listaDeImagens = imagens
        pass
    
    @property
    def animacao(self) -> Animacao:
        return self._animacao
    
    @animacao.setter
    def animacao(self, animacao: Animacao) -> None:
        self._animacao = animacao
        pass
    
    @property
    def alvo(self) -> Personagem:
        return self._alvo
    
    @alvo.setter
    def alvo(self, alvo: Personagem) -> None:
        self._alvo = alvo
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