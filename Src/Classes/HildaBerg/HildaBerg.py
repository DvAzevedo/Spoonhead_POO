import math
from Classes.HildaBerg.globalVar import*
from Classes.Animacao import *
from Classes.Personagem import *
from Classes.HildaBerg.HildaBergAtks import*
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.HildaBergDics import *
from Classes.HildaBerg.trajetoria import *
from Classes.cena import cena
from Classes.bars_indicators import *

#Attaks


#Hilda Build
class HildaBerg(Personagem):
    
    def __init__(self, x, y):
        super().__init__(x, y, 1000, HitBox(x, y, 50, 50))
        self.file = hildaIntro[0]
        self.state = STATE_LIST[0]
        self.animeClassList = [introAnime, normalAnime, laughAnime, tornadoAnime, dashIntroAnime, dashAnime, summonAnime, touroAnime, touroAtkAnime, transitionAnime]
        self.delayCount = Contador(ANIME_DELAY)
        self.count = 0
        self.isTouro = False
        self.isFinalBoss = False
        self.isDead = False
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
        
    def animateCase(self):
        if self.state == "dashIntro":
            self.animate()
            self.backToNormal(dashIntroAnime.ultimaImg, "dash")
            if self.file == dashIntroAnime.ultimaImg:
                DashSmoke(self.posX, self.posY)

        elif self.state == "dash":
            self.animate()
            if self.file == hildaDash[1] and self.estrelaFoiInstaciada == False:
                TouroStar(self.posX, self.posY)
                self.estrelaFoiInstaciada = True
            self.backToNormal(dashAnime.ultimaImg, "summon")
        
        elif self.state == "summon":
            self.animate()
            if self.file == hildaSummon[19] or self.file == hildaSummon[16]:
                DashExplo(self.posX, self.posY)
            self.backToNormal(summonAnime.ultimaImg, "touro")
            
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
                self.state = "moon_idle"
        
        elif self.state == "moon_idle":
            self.imune = False
            self.animate()
        
        else:
            self.animate()
        
    # Attaks
            
    def dash(self):
        if self.vida <= 750 and self.vida >= 500 and self.isTouro == False:
            self.isTouro = True
            if self.state == "normal":
                self.state = "dashIntro" 

    
    def ataca(self):
        risada(self)
        tornado(self)
        self.dash()
        touroAtk(self)

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
        if self.vida <= 250 and self.isFinalBoss == False: # Isso vai ser definido de acordo com a vida
            self.imune = True
            self.isFinalBoss = True
            self.state = "transition"
        if self.isDead == False and self.vida <= 0:
            self.vida = 0
            self.imune = True
            self.state = "moon_death"
        if self.vida <= 500 and self.state == "touro":
            DashExplo(self.posX, self.posY)
            self.state = "introFinal"
        

        if keyboard.is_key_just_down('l'):
            new_life_bar = Life_vilao(self, self.vida, self.posX, self.posY)