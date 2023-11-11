from tupy import *
class Cena:
    def __init__(self):#, viloes, heroi, viloes_attaks, heroi_attaks):
        self.viloes = None #viloes
        self.heroi = None #heroi
        self.viloes_attaks = None #viloes_attaks
        self.heroi_attaks = None #heroi_attaks

    def getVidaHeroi(self):
        return self.heroi.life
    def getVidaVilao(self, vilao):
        return vilao.life
    def getHeroiPosition(self):
        position = [self.heroi.x, self.heroi.y]
        return position
    def heroiFoiAtingido(self):
        pass
    def heroiSofreDano(self):
        self.heroi.life -=1
    def vilaoAtingido(self, vilao):
        pass
    def vilaoSofreDano(self, vilao):
        vilao.life -= 1

cena = Cena()