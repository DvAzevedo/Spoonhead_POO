from tupy import*
import math
from Classes.animacao import Contador
from HildaBerg.hildaImgLists import *
a = 100

class Animate:
    def __init__(self, maxUpdates, imgs):
        self._contador = Contador(maxUpdates)
        self._contador_de_imagens = Contador(maxUpdates)
        self.file = imgs[0]
        self.imgs = imgs
    def animate(self):
        self._contador.incrementa()
        self.file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        

class HildaBergNormal(Image):
    MAX_CONTADOR_UPDATES = 21
    MAX_CONTADOR_INTRO_UPDATES = 43
    def __init__(self, x, y):
        self.file = hildaIntro[0]
        self.estados = ["intro", "normal"]
        self.estado = self.estados[0]
        self.animateIntro = Animate(HildaBergNormal.MAX_CONTADOR_INTRO_UPDATES, hildaIntro)
        self.animateNormal = Animate(HildaBergNormal.MAX_CONTADOR_UPDATES, hildaNormal)
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(21)
        self.count = 0
        self.i = 1.5
        
    def updatePosition(self):
        self.i += 0.1
        self.x = (a * math.sqrt(2) * math.cos(self.i) * math.sin(self.i) / (1 + math.sin(self.i)**2)) +700
        self.y = (-a * math.sqrt(2) * math.cos(self.i) / (1 + math.sin(self.i)**2)) + 200

    def animate(self):
        if self.estado == "normal":
            self.animateNormal.animate()
            self.file = self.animateNormal.file
        elif self.estado == "intro":
            self.animateIntro.animate()
            self.file = self.animateIntro.file
            if self.count == 43:
                self.estado = "normal"
    #def risada(self):            
    def update(self):
        self.count +=1
        self.animate()
        if self.estado == "normal":
            self.updatePosition()
        if self.count == 500:
            self._hide()
            HildaBergNormalT(self.x, self.y)
            self.destroy()

class HildaBergNormalT(Image):
    MAX_CONTADOR_UPDATES = 48
    STATE = 0
    def __init__(self, x, y):
        self.file = hildaTransition[0]
        self.imgs = hildaTransition
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergNormalT.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(48)
        self.count = 0

    def update(self):
        self.count += 1
        self._contador.incrementa()
        self._file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        if self.count == 48:
            self._hide()
            HildaBergMoon(700, 220)
            self.destroy()

class HildaBergMoon(Image):
    MAX_CONTADOR_UPDATES = 16
    STATE = 0
    def __init__(self, x, y):
        self.file = hildaMoon[0]
        self.imgs = hildaMoon
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergMoon.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(16)
        self.count = 0

    def update(self):
        self._contador.incrementa()
        self._file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        self.count +=1
        if self.count == 50:
            self.destroy()

        