from tupy import *

class Ceu(Image):
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.velocidade = v
        self._file = "../Img/ceu.png"
    def update(self) -> None:
        if(self.x - self.velocidade) < -500:
            self.x = 1450

        else: self.x -= self.velocidade
        
class Chao(Image):
    def __init__(self, x, y, v):
        self.x = x 
        self.y = y 
        self.velocidade = v
        self._file = "../Img/chao.png"


    def update(self) -> None:
        if (self.x - self.velocidade) < -505:
            self.x = 1560
        else:
            self.x -= self.velocidade