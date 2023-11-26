import math
from Classes.HildaBerg.globalVar import*
from Classes.Animacao import *
from Classes.Personagem import *
from Classes.HildaBerg.HildaBergAtks import*
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.HildaBergDics import *
from Classes.HildaBerg.trajetoria import *
from Classes.HildaBerg.HildaBergLua import HildaBergLua
from Classes.HildaBerg.Ataques.Avanco import Avanco, Explosao
from Classes.HildaBerg.Ataques.Risada import Risada
from Classes.HildaBerg.Ataques.Tornado import Tornado
from Classes.cena import Cena
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
    STATE_LIST = ["intro", "normal", "laugh", "tornado", "dashIntro", "dash", "summon", "touro", "touroAtk", "transition"]
    ANIME_DELAY = 2
    def __init__(self, x, y):
        super().__init__(x, y, 1000, HitBox(x, y, 50, 50))
        self.file = hildaIntro[0]
        self.state = HildaBerg.STATE_LIST[0]
        self.introAnime = Animacao(QTD_IMGS_STATE_INTRO, hildaIntro, HildaBerg.ANIME_DELAY)
        self.normalAnime = Animacao(QTD_IMGS_STATE_NORMAL, hildaNormal, HildaBerg.ANIME_DELAY)
        self.laughAnime = Animacao(QTD_IMGS_STATE_LAUGH, hildaLaugh, 1)
        self.transitionAnime = Animacao(QTD_IMGS_STATE_TRANSITION, hildaTransition, HildaBerg.ANIME_DELAY)
        self.tornadoAnime = Animacao(QTD_IMGS_STATE_TORNADO, hildaTornado, 1)
        self.dashIntroAnime = Animacao(QTD_IMGS_STATE_DASH_INTRO, hildaDashIntro, 1)
        self.dashAnime = Animacao(QTD_IMGS_STATE_DASH, hildaDash, HildaBerg.ANIME_DELAY)
        self.summonAnime = Animacao(QTD_IMGS_STATE_SUMMON, hildaSummon, HildaBerg.ANIME_DELAY)
        self.touroAnime = Animacao(QTD_IMGS_STATE_TOURO, touroImgList, HildaBerg.ANIME_DELAY)
        self.touroAtkAnime = Animacao(QTD_IMGS_ATK_TOURO, touroAtkImgList, 1)
        self.animeClassList = [self.introAnime, self.normalAnime, self.laughAnime, self.tornadoAnime, self.dashIntroAnime, self.dashAnime, self.summonAnime, self.touroAnime,  self.touroAtkAnime, self.transitionAnime]
        self.delayCount = Contador(HildaBerg.ANIME_DELAY)
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
        if self.transitionAnime.imgsCont.contador > 37 and self.transitionAnime.imgsCont.contador < QTD_IMGS_STATE_TRANSITION:
            self.posX += (X_POSITION_ORIGIN - self.posX) / (QTD_IMGS_STATE_TRANSITION - self.transitionAnime.imgsCont.contador)
            self.posY += (Y_POSITION_ORIGIN - self.posY) / (QTD_IMGS_STATE_TRANSITION - self.transitionAnime.imgsCont.contador)
    
    def dashUpdatePosition(self):
        self.posX -= 60
    
    def touroAtkUpdatePosition(self):
        result = any(self.file == touroAtkImgList[i] for i in range(10, 21))
        if result:
            self.posX -= 50
            pass
        self.posX += 3
        pass
    
    def movimento_de_avanco(self) -> None:
        self.posX -= 60
        pass
    
    def movimento_de_transicao(self) -> None:
        if self.animacaoDeTransicao.imgsCont.contador > 37 and self.animacaoDeTransicao.imgsCont.contador < QTD_IMGS_ESTADO_TRANSICAO:
            self.posX += (ORIGEM_X - self.posX) / (QTD_IMGS_ESTADO_TRANSICAO - self.animacaoDeTransicao.imgsCont.contador)
            self.posY += (ORIGEM_Y - self.posY) / (QTD_IMGS_ESTADO_TRANSICAO - self.animacaoDeTransicao.imgsCont.contador)
        pass 
    
    def movimento_padrao(self) -> None:
        self.angulacao += 0.1
        self.posX = ((100 * math.sqrt(2) * math.cos(self.angulacao) * math.sin(self.angulacao) / (1 + math.sin(self.angulacao)**2)) + ORIGEM_X) 
        self.posY = ((-100 * math.sqrt(2) * math.cos(self.angulacao) / (1 + math.sin(self.angulacao)**2)) + ORIGEM_Y)
        #self.teste_barraDeVida._x = self.posX + self.teste_barraDeVida.x0
        #self.teste_barraDeVida._y = self.posY + self.teste_barraDeVida.y0
        pass 
    
    def movimento_summonando(self) -> None:
        self.posX += 16
        pass

    #Animações
    def animacao_finalizada(self, ultimaImg: str) -> bool:
        if self.file == ultimaImg:
            return True
        
    def backToNormal(self, lastImg, state):
        if self.file == lastImg:
            self.state = state

    def animate(self, indice):
        self.animeClassList[indice].animar()
        self.file = self.animeClassList[indice].imagem
        
    def animateCase(self):# Mudar para switch case
        if self.state == "intro":
            self.animate(0)
            self.backToNormal(self.introAnime.ultimaImg, "normal")

        elif self.state == "normal":
            self.animate(1)

        elif self.state == "laugh":
            self.animate(2)
            self.backToNormal(self.laughAnime.ultimaImg, "normal")
    
        elif self.state == "tornado":
            self.animate(3)
            self.backToNormal(self.tornadoAnime.ultimaImg, "normal")

        elif self.state == "dashIntro":
            self.animate(4)
            self.backToNormal(self.dashIntroAnime.ultimaImg, "dash")
            if self.file == self.dashIntroAnime.ultimaImg:
                DashSmoke(self.posX, self.posY)

        elif self.state == "dash":
            self.animate(5)
            if self.file == hildaDash[1] and self.estrelaFoiInstaciada == False:
                TouroStar(self.posX, self.posY)
                self.estrelaFoiInstaciada = True
            self.backToNormal(self.dashAnime.ultimaImg, "summon")
        
        elif self.state == "summon":
            self.animate(6)
            if self.file == hildaSummon[19] or self.file == hildaSummon[16]:
                DashExplo(self.posX, self.posY)
            self.backToNormal(self.summonAnime.ultimaImg, "touro")
        
        elif self.state == "touro":
            self.animate(7)
            #self.backToNormal(self.touroAnime.lastImg, "normal")
            
        elif self.state == "touroAtk":
            self.animate(8)
            if self.file == self.touroAtkAnime.ultimaImg: # Gambiarra para touro chegar pra trás
                self.posX += 30
                self.estrelaFoiInstaciada = False
            if self.estrelaFoiInstaciada == False:
                self.backToNormal(self.touroAtkAnime.ultimaImg, "touro")
        
        elif self.state == "transition":
            self.animate(9)
            if self.isAnimeFinish(self.transitionAnime.ultimaImg):
                self._hide()
                HildaBergLua(X_POSITION_ORIGIN, Y_POSITION_ORIGIN)
                self.destroy()

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
        self.animateCase()
        self.movimenta()
        self.hitbox.atualiza_posicao(self.posX, self.posY)
        self.atualiza_label_life()
        if self.count == 800: # Isso vai ser definido de acordo com a vida
            self.state = "transition"
        if keyboard.is_key_just_down('l'):
            new_life_bar = Life_vilao(self, self.vida, self.posX, self.posY)
