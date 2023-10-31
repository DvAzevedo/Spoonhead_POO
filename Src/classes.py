from tupy import*
from enum import Enum
import math


# class Trajetoria():
#     def seno(x, y, helper):
#         helper += 0.1
#         x += 5
#         y = (math.sin(helper)*250) + 250
        
class Projetil(Image):
    def __init__(self, x, y, image, helper):#, trajetoria):
        self.file = image
        self.x = x 
        self.y = y
        self.helper = helper
    def seno(self):
        self.helper += 0.1
        self.x -= 10
        self.y = ((math.sin(self.helper)*250) + 250)


class Arma():
    def __init__(self, qtd_municao, delay, projetil):
        self.municoes = []
        self.projetil = projetil
        self.delay = delay
        self.qtd_municao = qtd_municao
        self.redefine()
    def atirar(self):
        for i in range(self.qtd_municao):
            self.municoes[i].seno()
    def redefine(self):
        for i in range(self.qtd_municao):
            currentDelay = self.delay*i
            currentX = self.projetil.x +((20*i)/4)
            self.municoes.append(Projetil(currentX, self.projetil.y, self.projetil.file, self.projetil.helper - currentDelay))


class Personagem(Image):
    def __init__(self, x, y, image, life, armas):
        self.file = image
        self.x = x
        self.y = y
        self.life = life
        self.armas = armas

class Vilao_test_1(Personagem):
    def __init__(self, x, y, image, life, armas):
        super().__init__(x, y, image, life, armas)
        self.atirando = False
        self.currentArma = armas[0]
    def comecarAtirar(self):
        if keyboard.is_key_just_down('space'):
            self.atirando = True
    def update(self):
        self.comecarAtirar()
        if self.atirando == True:
            self.currentArma.atirar()
            if self.currentArma.municoes[self.currentArma.qtd_municao-1].x < 0:
                self.currentArma.redefine()
                

pedra = Projetil(800, 250, "../Img/pedra_poo.png", -0.2)
sennno = Arma(20, 0.05, pedra)
vi = Vilao_test_1(800, 300, "../Img/balaoVerde_poo.webp", 200, [sennno])
run(globals())


