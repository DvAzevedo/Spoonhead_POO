from tupy import*
import math
from Classes.animacao import Contador, Animate
from HildaBerg.hildaImgLists import *
from Classes.cena import cena
a = 100 #Mudar nome
Y_POSITION_ORIGIN = 240
X_POSITION_ORIGIN = 700

QTD_IMGS_STATE_NORMAL = 21
QTD_IMGS_STATE_LAUGH = 19
QTD_IMGS_STATE_INTRO = 43
QTD_IMGS_STATE_TRANSITION = 48
QTD_IMGS_STATE_TORNADO = 38

QTD_IMGS_STATE_HA = 46
QTD_IMGS_STATE_TORNADO_ATK = 16
QTD_IMGS_STATE_TORNADO_INTRO_ATK = 12

#Attaks
class Ha(Image):
    
    ANIME_DELAY = 1
    def __init__(self, x, y):
        self.file = imgListHa[0]
        self.animateHa = Animate(QTD_IMGS_STATE_HA, imgListHa, Ha.ANIME_DELAY)
        self.x = x
        self.y = y
        self.yo = y
        self.sin = -1

    def trajetoria(self):
        self.sin += 1
        self.x -= 20
        self.y = ((math.sin(self.sin)*5)+Y_POSITION_ORIGIN)

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

    

class Tornado(Image):
    ANIME_DELAY = 2
    def __init__(self, x, y):
        self.file = hildaTornadoAtkIntro[0]
        self.introAnime = Animate(QTD_IMGS_STATE_TORNADO_INTRO_ATK, hildaTornadoAtkIntro, 3)
        self.atkAnime = Animate(QTD_IMGS_STATE_TORNADO_ATK, hildaTornadoAtk, Tornado.ANIME_DELAY)
        self.currentAnime = self.introAnime
        self.x = x - 80
        self.y = y
        self.heroi_x = cena.getHeroiPosition()[0]
        self.heroi_y = cena.getHeroiPosition()[1]
        self.praCima = False
        if self.heroi_y > self.y:
            self.praCima = True

    def trajetoria(self):
        if self.currentAnime == self.atkAnime:
            if self.x > self.heroi_x:
                self.x -= ((self.x - self.heroi_x )/ 30) + 5
                self.y -= ((self.y - self.heroi_y )/ 30)
            else:
                self.x -= 5
                if self.praCima:
                    self.y += 2
                else:
                    self.y -=2

    def animate(self):
        self.file = self.currentAnime.anima()

    def changeAnimate(self):
        if self.file == self.introAnime.lastImg:
            self.currentAnime = self.atkAnime

    def destruir(self):
        if self.x < -20:
            self.destroy()

    def update(self):
        self.trajetoria()
        self.changeAnimate()
        self.animate()
        self.destruir()


#Hilda Build
class HildaBerg(Image):
    STATE_LIST = ["intro", "normal", "laugh", "tornado", "transition"]
    ANIME_DELAY = 2
    def __init__(self, x, y):
        self.file = hildaIntro[0]
        self.x = x
        self.y = y
        self.state = HildaBerg.STATE_LIST[0]
        self.introAnime = Animate(QTD_IMGS_STATE_INTRO, hildaIntro, HildaBerg.ANIME_DELAY)
        self.normalAnime = Animate(QTD_IMGS_STATE_NORMAL, hildaNormal, HildaBerg.ANIME_DELAY)
        self.laughAnime = Animate(QTD_IMGS_STATE_LAUGH, hildaLaugh, 1)
        self.transitionAnime = Animate(QTD_IMGS_STATE_TRANSITION, hildaTransition, HildaBerg.ANIME_DELAY)
        self.tornadoAnime = Animate(QTD_IMGS_STATE_TORNADO, hildaTornado, 1)
        self.animeClassList = [self.introAnime, self.normalAnime, self.laughAnime, self.tornadoAnime, self.transitionAnime]
        self.delayCount = Contador(HildaBerg.ANIME_DELAY)
        self.count = 0
        self.life = 1000
        self.i = 1.5

    # Positions Update    
    def normalUpdatePosition(self):
        self.i += 0.1
        self.x = ((a * math.sqrt(2) * math.cos(self.i) * math.sin(self.i) / (1 + math.sin(self.i)**2)) + X_POSITION_ORIGIN) 
        self.y = ((-a * math.sqrt(2) * math.cos(self.i) / (1 + math.sin(self.i)**2)) + Y_POSITION_ORIGIN)
    
    def transitionUpdatePosition(self):
        if self.transitionAnime.getImgCount() > 37 and self.transitionAnime.getImgCount() < QTD_IMGS_STATE_TRANSITION:
            self.x += (X_POSITION_ORIGIN - self.x) / (QTD_IMGS_STATE_TRANSITION - self.transitionAnime.getImgCount())
            self.y += (Y_POSITION_ORIGIN - self.y) / (QTD_IMGS_STATE_TRANSITION - self.transitionAnime.getImgCount())
    
    def updatePosition(self):
        if self.state == "normal" or self.state == "laugh":
            self.normalUpdatePosition()   
        if self.state == "transition":
            self.transitionUpdatePosition()

    # Animations
    def isAnimeFinish(self, lastImg):
        if self.file == lastImg:
            return True
        
    def backToNormal(self, lastImg):
        if self.file == lastImg:
            self.state = "normal"

    def animate(self, indice):
        self.animeClassList[indice].animate()
        self.file = self.animeClassList[indice].file
        
    def animateCase(self):# Mudar para switch case
        if self.state == "intro":
            self.animate(0)
            self.backToNormal(self.introAnime.lastImg)

        elif self.state == "normal":
            self.animate(1)

        elif self.state == "laugh":
            self.animate(2)
            self.backToNormal(self.laughAnime.lastImg)

    
        elif self.state == "tornado":
            self.animate(3)
            self.backToNormal(self.tornadoAnime.lastImg)
        
        elif self.state == "transition":
            self.animate(4)
            if self.isAnimeFinish(self.transitionAnime.lastImg):
                self._hide()
                HildaBergMoon(X_POSITION_ORIGIN, Y_POSITION_ORIGIN)
                self.destroy()
    # Attaks
    def risada(self):
        if keyboard.is_key_just_down('r'):
            if self.state == "normal":
                Ha(self.x, self.y)
                self.state = "laugh" 
    
    def tornado(self):
        if keyboard.is_key_just_down('t'):
            if self.state == "normal":
                Tornado(self.x, self.y)
                self.state = "tornado" 
            

    def update(self):
        self.count +=1
        self.risada()
        self.tornado()
        self.animateCase()
        self.updatePosition()
        if self.count == 300: # Isso vai ser definido de acordo com a vida
            self.state = "transition"
            
        

class HildaBergMoon(Image):
    QTD_IMG_STATE_NORMAL = 16
    ANIME_DELAY = 2
    STATE = 0
    def __init__(self, x, y):
        self.file = hildaMoon[0]
        self.imgs = hildaMoon
        self.x = x
        self.y = y
        self.normalAnime = Animate(HildaBergMoon.QTD_IMG_STATE_NORMAL, hildaMoon, HildaBergMoon.ANIME_DELAY)
        self.count = 0

    def update(self):
        self.normalAnime.animate()
        self.file = self.normalAnime.file