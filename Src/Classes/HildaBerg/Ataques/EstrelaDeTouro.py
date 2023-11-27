from Classes.Animacao import Animacao
from Classes.Ataque import *
from Classes.HildaBerg.listasDeImagens import touroStarImgList
from Classes.Personagem import Personagem

class EstrelaDeTouro(Ataque):
    ATRASO_DE_ANIMACAO = 1
    QTD_IMAGENS = 3
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(EstrelaDeTouro.QTD_IMAGENS, touroStarImgList, EstrelaDeTouro.ATRASO_DE_ANIMACAO), 0)
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
        pass
    
    def causa_dano(self) -> None:
        pass
    
    def update(self) -> None:
        self.file = self.animacao.anima()
        if self.incrementador == 16:
            self.destroy()
        self.incrementador += 1
        pass
