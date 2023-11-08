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

#Attaks

#         self.helper += 0.1
#         self.x -= 10
#         self.y = ((math.sin(self.helperSeno)*75)+self.aux_y)
class Ha(Image):
    MAX_CONTADOR_UPDATES = 13
    def __init__(self, x, y):
        self.file = imgListHa[0]
        self.animateHa = Animate(Ha.MAX_CONTADOR_UPDATES, imgListHa)
        self.x = x
        self.y = y
        self.yo = y
        self.sin = -1

    def trajetoria(self):
        self.sin += 1
        self.x -= 60
        self.y = ((math.sin(self.sin)*30)+self.yo)

    def animate(self):
        self.animateHa.animate()
        self.file = self.animateHa.file

    def destruir(self):
        if self.x < -20:
            self.destroy()

    def update(self):
        self.trajetoria()
        self.animate()
        self.destruir()




#Hilda Build
class HildaBergNormal(Image):
    MAX_CONTADOR_UPDATES = 21
    MAX_CONTADOR_UPDATES_LOUGH = 13
    MAX_CONTADOR_INTRO_UPDATES = 43
    def __init__(self, x, y):
        self.file = hildaIntro[0]
        self.estados = ["intro", "normal", "lough"]
        self.estado = self.estados[0]
        self.animateIntro = Animate(HildaBergNormal.MAX_CONTADOR_INTRO_UPDATES, hildaIntro)
        self.animateNormal = Animate(HildaBergNormal.MAX_CONTADOR_UPDATES, hildaNormal)
        self.animateLough = Animate(HildaBergNormal.MAX_CONTADOR_UPDATES_LOUGH, hildaLaugh)
        self.x = x
        self.y = y
        self.count = 0
        self.i = 1.5
        
    def updatePosition(self):
        self.i += 0.1
        self.x = (a * math.sqrt(2) * math.cos(self.i) * math.sin(self.i) / (1 + math.sin(self.i)**2)) +700
        self.y = (-a * math.sqrt(2) * math.cos(self.i) / (1 + math.sin(self.i)**2)) + 200

    def animate(self):
        if self.estado == "intro":
            self.animateIntro.animate()
            self.file = self.animateIntro.file
            if self.count == HildaBergNormal.MAX_CONTADOR_INTRO_UPDATES:
                self.estado = "normal"
                self.count = 0

        elif self.estado == "lough":
            self.animateLough.animate()
            self.file = self.animateLough.file
            if self.count == HildaBergNormal.MAX_CONTADOR_UPDATES_LOUGH:
                self.estado = "normal"
                self.count = 0

        elif self.estado == "normal":
            self.animateNormal.animate()
            self.file = self.animateNormal.file

    def risada(self):
        if keyboard.is_key_just_down('h'):
            self.estado = "lough" 
            self.count = 0 
            Ha(self.x, self.y)

    def update(self):
        self.count +=1
        self.risada()
        self.animate()
        if self.estado == "normal":
            self.updatePosition()   
        if self.count == 100:
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
        self.xh = (700 - self.x) / 11
        self.yh = (220 - self.y) / 11

    def update(self):
        self.count += 1
        self._contador.incrementa()
        self._file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        if self.count > 38:
            self.x += self.xh
            self.y += self.yh
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
        if self.count == 500:
            self.destroy()