from tupy import *
from Classes.Personagem import Personagem
class Cena:
    def __init__(self, heroi: Personagem, vilao: Personagem) -> None:#, viloes, heroi, viloes_attaks, heroi_attaks):
        self.vilao = vilao #viloes
        self.heroi = heroi #heroi
        self.viloes_attaks = None #viloes_attaks
        self.heroi_attaks = None #heroi_attaks

    def getVidaHeroi(self) -> int:
        return self.heroi.vida
    def getVidaVilao(self) -> int:
        return self.vilao.vida
    def getHeroiPosition(self) -> list[int]:
        position = [self.heroi.x, self.heroi.y]
        return position
    def heroiFoiAtingido(self)-> None:
        pass
    def heroiSofreDano(self)-> None:
        self.heroi.vida -=1
    def vilaoAtingido(self)-> None:
        pass
    def vilaoSofreDano(self)-> None:
        self.vilao.vida -= 1