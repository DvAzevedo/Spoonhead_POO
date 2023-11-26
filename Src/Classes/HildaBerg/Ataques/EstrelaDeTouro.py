from Classes.Animacao import Animacao
from Classes.Ataque import *
from Classes.HildaBerg.listasDeImagens import touroStarImgList
from Classes.Personagem import Personagem

class EstrelaDeTouro(Ataque):
    ANIME_DELAY = 1
    QTD_IMGS_STAR_TOURO = 3
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(EstrelaDeTouro.QTD_IMGS_STAR_TOURO, touroStarImgList, EstrelaDeTouro.ANIME_DELAY), 1)
        self.posX -= 30
        self._incrementador = 0
        pass
    
    @property
    def incrementador(self) -> int:
        return self._incrementador
    
    @incrementador.setter
    def incrementador(self, incremento: int) -> None:
        self._incrementador = incremento
        pass
    
    def atualiza_coordenadas(self) -> None:
        if self.incrementador == 16:
            self.destroy()
        pass
    
    def causa_dano(self) -> None:
        pass
    
    def update(self) -> None:
        self.file = self.animacao.anima()
        self.atualiza_coordenadas()
        self.incrementador += 1
        pass
