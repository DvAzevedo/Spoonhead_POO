import math
from tupy import*
from Classes.HildaBerg.globalVar import*
from Classes.Animacao import *
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.trajetoria import *
from Classes.cena import*

Y_POSITION_ORIGIN = 240
X_POSITION_ORIGIN = 700

QTD_IMGS_STATE_TOURO = 16
QTD_IMGS_STAR_TOURO = 3
QTD_IMGS_ATK_TOURO = 21

QTD_IMGS_ATK_HA = 46
QTD_IMGS_ATK_TORNADO = 16
QTD_IMGS_ATK_TORNADO_INTRO = 12
QTD_IMGS_ATK_DASH_EXPLO = 15
QTD_IMGS_ATK_DASH_SMOKE = 6 

class Ha(Image):
    
    ANIME_DELAY = 1
    def __init__(self, x, y):
        self.file = imgListHa[0]
        self.animateHa = Animacao(QTD_IMGS_ATK_HA, imgListHa, Ha.ANIME_DELAY)
        self.x = x
        self.y = y
        self.yo = y
        self.sin = -1

    def trajetoria(self):
        self.sin += 1
        self.x -= 20
        self.y = ((math.sin(self.sin)*5)+Y_POSITION_ORIGIN)

    def animate(self):
        self.animateHa.animar()
        self.file = self.animateHa.imagem

    def destruir(self):
        if self.x < -20:
            self.destroy()

    def update(self):
        self.trajetoria()
        self.animate()
        self.destruir()

    

class Tornado(Image):
    ANIME_DELAY = 1
    def __init__(self, x, y):
        self.file = hildaTornadoAtkIntro[0]
        self.introAnime = Animacao(QTD_IMGS_ATK_TORNADO_INTRO, hildaTornadoAtkIntro, 2)
        self.atkAnime = Animacao(QTD_IMGS_ATK_TORNADO, hildaTornadoAtk, Tornado.ANIME_DELAY)
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
                self.x -= ((self.x - self.heroi_x )/ 30) + 10
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
        if self.file == self.introAnime.ultimaImg:
            self.currentAnime = self.atkAnime

    def destruir(self):
        if self.x < -20:
            self.destroy()

    def update(self):
        self.trajetoria()
        self.changeAnimate()
        self.animate()
        self.destruir()

class DashSmoke(Image):
    ANIME_DELAY = 2
    def __init__(self, x, y):
        self.file = dashSmoke[0]
        self.dashSmokeAnime = Animacao(QTD_IMGS_ATK_DASH_SMOKE, dashSmoke, DashSmoke.ANIME_DELAY)
        self.x = x + 190
        self.y = y + 13

    def trajetoria(self):
        self.x -= 60

    def animate(self):
        self.file = self.dashSmokeAnime.anima()

    def destruir(self):
        if self.file == self.dashSmokeAnime.ultimaImg:
            self.destroy()

    def update(self):
        self.trajetoria()
        self.animate()
        self.destruir()

class DashExplo(Image):
    ANIME_DELAY = 2
    def __init__(self, x, y):
        self.file = dashExplo[0]
        self.dashExploAnime = Animacao(QTD_IMGS_ATK_DASH_EXPLO, dashExplo, DashExplo.ANIME_DELAY)
        self.x = x 
        self.y = y 
        self.theta = np.linspace(0, 30 * np.pi, 30)
        self.a = 1
        self.b = 1
        self.count = 0
    
    def trajetoria(self):
        coor = archimedean_spiral(self.theta[self.count], self.a, self.b)
        self.x = coor[0] + X_POSITION_ORIGIN
        self.y = coor[1] + Y_POSITION_ORIGIN
        self.count += 1

    def animate(self):
        self.file = self.dashExploAnime.anima()

    def destruir(self):
        if self.file == self.dashExploAnime.ultimaImg:
            self.destroy()

    def update(self):
        self.trajetoria()
        self.animate()
        self.destruir()

class TouroStar(Image):
    ANIME_DELAY = 1
    def __init__(self, x, y):
        self.file = touroStarImgList[0]
        self.touroStarAnime = Animacao(QTD_IMGS_STAR_TOURO, touroStarImgList, TouroStar.ANIME_DELAY)
        self.x = x - 30
        self.y = y
        self.count = 0

    def animate(self):
        self.file = self.touroStarAnime.anima()

    def destruir(self):
        if self.count == 16:
            self.destroy()

    def update(self):
        self.animate()
        self.count += 1
        self.destruir()

def risada(hilda):
    if keyboard.is_key_just_down('r'):
        if hilda.state == "normal":
            Ha(hilda.posX, hilda.posY)
            hilda.state = "laugh" 

def tornado(hilda):
    if keyboard.is_key_just_down('t'):
        if hilda.state == "normal":
            Tornado(hilda.posX, hilda.posY)
            hilda.state = "tornado" 

def touroAtk(hilda):
    if keyboard.is_key_just_down('c'):
        if hilda.state == "touro":
            hilda.state = "touroAtk"

def ovn(hilda):
    pass