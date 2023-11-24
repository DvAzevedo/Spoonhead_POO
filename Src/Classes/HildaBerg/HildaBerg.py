import math
from Classes.Animacao import *
from Classes.Personagem import *
from Classes.HildaBerg.HildaBergLua import HildaBergLua
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.trajetoria import *
from Classes.cena import cena
from Classes.bars_indicators import *

Y_POSITION_ORIGIN = 240
X_POSITION_ORIGIN = 700

QTD_IMGS_STATE_NORMAL = 21
QTD_IMGS_STATE_LAUGH = 19
QTD_IMGS_STATE_INTRO = 43
QTD_IMGS_STATE_TRANSITION = 48
QTD_IMGS_STATE_TORNADO = 38
QTD_IMGS_STATE_DASH_INTRO = 18
QTD_IMGS_STATE_DASH = 6
QTD_IMGS_STATE_SUMMON = 21

QTD_IMGS_STATE_TOURO = 16
QTD_IMGS_STAR_TOURO = 3
QTD_IMGS_ATK_TOURO = 21

QTD_IMGS_ATK_HA = 46
QTD_IMGS_ATK_TORNADO = 16
QTD_IMGS_ATK_TORNADO_INTRO = 12
QTD_IMGS_ATK_DASH_EXPLO = 15
QTD_IMGS_ATK_DASH_SMOKE = 6
ANIME_DELAY = 2

STATE_LIST = ["intro", "normal", "laugh", "tornado", "dashIntro", "dash", "summon", "touro", "touroAtk", "transition"]

introAnime = Animacao(QTD_IMGS_STATE_INTRO, hildaIntro, ANIME_DELAY, True, "normal")
normalAnime = Animacao(QTD_IMGS_STATE_NORMAL, hildaNormal, ANIME_DELAY)
laughAnime = Animacao(QTD_IMGS_STATE_LAUGH, hildaLaugh, 1, True, "normal")
transitionAnime = Animacao(QTD_IMGS_STATE_TRANSITION, hildaTransition, ANIME_DELAY)
tornadoAnime = Animacao(QTD_IMGS_STATE_TORNADO, hildaTornado, 1, True, "normal")
dashIntroAnime = Animacao(QTD_IMGS_STATE_DASH_INTRO, hildaDashIntro, 1, True, "dash")
dashAnime = Animacao(QTD_IMGS_STATE_DASH, hildaDash, ANIME_DELAY, True, "summon")
summonAnime = Animacao(QTD_IMGS_STATE_SUMMON, hildaSummon, ANIME_DELAY, True, "touro")
touroAnime = Animacao(QTD_IMGS_STATE_TOURO, touroImgList, ANIME_DELAY)
touroAtkAnime = Animacao(QTD_IMGS_ATK_TOURO, touroAtkImgList, 1, True, "touro")

QTD_IMG_MOON_STATE_NORMAL = 16
QTD_IMG_MOON_STATE_ATK_INTRO = 12
QTD_IMG_MOON_STATE_ATK = 8
QTD_IMG_MOON_STATE_ATK_BACK = 8
QTD_IMG_MOON_STATE_SMOKE = 15
QTD_IMG_MOON_STATE_DEATH = 16
ANIME_DELAY_MOON = 2

MOON_STATE_LIST = ["idle", "atkIntro", "atk", "death"]

moon_idleAnime = Animacao(QTD_IMG_MOON_STATE_NORMAL, hildaMoon, ANIME_DELAY_MOON)
moon_atkIntroAnime = Animacao(QTD_IMG_MOON_STATE_ATK_INTRO, moonAtkIntro, ANIME_DELAY_MOON)
moon_atkAnime = Animacao(QTD_IMG_MOON_STATE_ATK, moonAtk, ANIME_DELAY_MOON)
moon_atkBackAnime = Animacao(QTD_IMG_MOON_STATE_ATK_BACK, moonAtkBack, ANIME_DELAY_MOON)
moon_smokeAnime = Animacao(QTD_IMG_MOON_STATE_SMOKE, moonSmoke, ANIME_DELAY_MOON)
moon_deathAnime = Animacao(QTD_IMG_MOON_STATE_DEATH, moonDeath, ANIME_DELAY_MOON)


STATE_LIST = ["intro", "normal", "laugh", "tornado", "dashIntro", "dash", "summon", "touro", "touroAtk", "transition"]

STATE_DIC = {
    "intro": introAnime,
    "normal": normalAnime,
    "laugh": laughAnime,
    "tornado": tornadoAnime,
    "dashIntro": dashIntroAnime,
    "dash": dashAnime,
    "summon": summonAnime,
    "touro": touroAnime,
    "touroAtk": touroAtkAnime,
    "transition": transitionAnime,
    "moon_idle": moon_idleAnime,
    "moon_atkIntro": moon_atkIntroAnime,
    "moon_atk": moon_atkAnime,
    "moon_atkBack": moon_atkBackAnime,  
    "moon_smoke": moon_smokeAnime,
    "moon_death": moon_deathAnime
}

#Attaks
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

#Hilda Build
class HildaBerg(Personagem):
    
    def __init__(self, x, y):
        super().__init__(x, y, 1000, HitBox(x, y, 50, 50))
        self.file = hildaIntro[0]
        self.state = STATE_LIST[0]
        self.animeClassList = [introAnime, normalAnime, laughAnime, tornadoAnime, dashIntroAnime, dashAnime, summonAnime, touroAnime, touroAtkAnime, transitionAnime]
        self.delayCount = Contador(ANIME_DELAY)
        self.count = 0
        #self.life = 1000
        self.i = 1.5
        self.estrelaFoiInstaciada = False
        # DEFINICAO DA VIDA DE HILDA E IMAGEM
        self.test_life_bar = Life_vilao(self, self.vida, self.posX, self.posY)

    # Positions Update    
    def normalUpdatePosition(self):
        self.i += 0.1
        self.posX = ((100 * math.sqrt(2) * math.cos(self.i) * math.sin(self.i) / (1 + math.sin(self.i)**2)) + X_POSITION_ORIGIN) 
        self.posY = ((-100 * math.sqrt(2) * math.cos(self.i) / (1 + math.sin(self.i)**2)) + Y_POSITION_ORIGIN)
        self.test_life_bar._x = self.posX + self.test_life_bar.x0
        self.test_life_bar._y = self.posY + self.test_life_bar.y0
    
    def transitionUpdatePosition(self):
        if transitionAnime.imgsCont.contador > 37 and transitionAnime.imgsCont.contador < QTD_IMGS_STATE_TRANSITION:
            self.posX += (X_POSITION_ORIGIN - self.posX) / (QTD_IMGS_STATE_TRANSITION - transitionAnime.imgsCont.contador)
            self.posY += (Y_POSITION_ORIGIN - self.posY) / (QTD_IMGS_STATE_TRANSITION - transitionAnime.imgsCont.contador)
    
    def dashUpdatePosition(self):
        self.posX -= 60
    
    def touroAtkUpdatePosition(self):
        result = any(self.file == touroAtkImgList[i] for i in range(10, 21))
        if result:
            self.posX -= 50
        else:
            self.posX += 3
    
    def summonUpdatePosition(self):
        self.posX += 16

    def movimenta(self) -> None:
        if self.state == "normal" or self.state == "laugh" or self.state == "touro":
            self.normalUpdatePosition()   
        if self.state == "dash":
            self.dashUpdatePosition()
        if self.state == "touroAtk":
            self.touroAtkUpdatePosition()
        if self.state == "summon":
            self.summonUpdatePosition()
        if self.state == "transition":
            self.transitionUpdatePosition()
        pass

    # Animations
    def isAnimeFinish(self, lastImg):
        if self.file == lastImg:
            return True
        
    def backToNormal(self, lastImg, state):
        if self.file == lastImg:
            self.state = state

    def animate(self):
        STATE_DIC[self.state].animar()
        self.file = STATE_DIC[self.state].imagem
        if STATE_DIC[self.state].backToState():
                 self.state = introAnime.backToState()
        
    def animateCase(self):# Mudar para switch case
        if self.state == "intro":
            self.animate()
            
        elif self.state == "normal":
            self.animate()
            
        elif self.state == "laugh":
            self.animate()
    
        elif self.state == "tornado":
            self.animate()

        elif self.state == "dashIntro":
            self.animate()
            self.backToNormal(dashIntroAnime.ultimaImg, "dash")
            if self.file == dashIntroAnime.ultimaImg:
                DashSmoke(self.posX, self.posY)

        elif self.state == "dash":
            self.animate()
            if self.file == hildaDash[1] and self.estrelaFoiInstaciada == False:
                TouroStar(self.posX, self.posY)
                self.estrelaFoiInstaciada = True
            # self.animate()
            self.backToNormal(dashAnime.ultimaImg, "summon")
        
        elif self.state == "summon":
            self.animate()
            if self.file == hildaSummon[19] or self.file == hildaSummon[16]:
                DashExplo(self.posX, self.posY)
            # self.animate()
            self.backToNormal(summonAnime.ultimaImg, "touro")
        
        elif self.state == "touro":
            self.animate()
            #self.backToNormal(self.touroAnime.lastImg, "normal")
            
        elif self.state == "touroAtk":
            self.animate()
            if self.file == touroAtkAnime.ultimaImg: # Gambiarra para touro chegar pra trás
                self.posX += 30
                self.estrelaFoiInstaciada = False
            if self.estrelaFoiInstaciada == False:
                self.backToNormal(touroAtkAnime.ultimaImg, "touro")
        
        elif self.state == "transition":
            self.animate()
            if self.isAnimeFinish(transitionAnime.ultimaImg):
                self.state = "moon"
                self.imune = False
                

    # Attaks
    def risada(self):
        if keyboard.is_key_just_down('r'):
            if self.state == "normal":
                Ha(self.posX, self.posY)
                self.state = "laugh" 
    
    def tornado(self):
        if keyboard.is_key_just_down('t'):
            if self.state == "normal":
                Tornado(self.posX, self.posY)
                self.state = "tornado" 
            
    def dash(self):
        if keyboard.is_key_just_down('d'):
            if self.state == "normal":
                self.state = "dashIntro" 

    def touroAtk(self):
        if keyboard.is_key_just_down('c'):
            if self.state == "touro":
                self.state = "touroAtk" 
    
    def ataca(self):
        self.risada()
        self.tornado()
        self.dash()
        self.touroAtk()

    def atualiza_label_life(self):
        if self.vida != self.test_life_bar.life:
            self.test_life_bar.label.text = str(self.vida)
            self.test_life_bar._rectangle._width = self.test_life_bar.label._width
            self.test_life_bar._rectangle._height = self.test_life_bar.label._height

    def update(self):
        self.count +=1
        self.ataca()
        #self.animate()
        self.animateCase()
        self.movimenta()
        self.hitbox.atualiza_posicao(self.posX, self.posY)
        self.atualiza_label_life()
        if self.vida <= 450: # Isso vai ser definido de acordo com a vida
            self.imune = True
            self.state = "transition"

        if keyboard.is_key_just_down('l'):
            new_life_bar = Life_vilao(self, self.vida, self.posX, self.posY)