from tupy import*
from Classes.Animacao import Animacao
from Classes.Personagem import Personagem
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.trajetoria import *
from Classes.bars_indicators import *

QTD_IMG_STATE_NORMAL = 16
QTD_IMG_STATE_ATK_INTRO = 12
QTD_IMG_STATE_ATK = 8
QTD_IMG_STATE_ATK_BACK = 8
QTD_IMG_STATE_SMOKE = 15
QTD_IMG_STATE_DEATH = 16
ANIME_DELAY = 2

idleAnime = Animacao(QTD_IMG_STATE_NORMAL, hildaMoon, ANIME_DELAY)
atkIntroAnime = Animacao(QTD_IMG_STATE_ATK_INTRO, moonAtkIntro, ANIME_DELAY)
atkAnime = Animacao(QTD_IMG_STATE_ATK, moonAtk, ANIME_DELAY)
atkBackAnime = Animacao(QTD_IMG_STATE_ATK_BACK, moonAtkBack, ANIME_DELAY)
smokeAnime = Animacao(QTD_IMG_STATE_SMOKE, moonSmoke, ANIME_DELAY)
deathAnime = Animacao(QTD_IMG_STATE_DEATH, moonDeath, ANIME_DELAY)

class HildaBergLua(Personagem):
    
    STATE = 0
    
    def __init__(self, x, y):
        self.file = hildaMoon[0]
        self.imgs = hildaMoon
        self.x = x
        self.y = y
        self.count = 0

    def ataca(self):
        return super().ataca()

    def movimenta(self):
        return super().movimenta()

    def update(self):
        idleAnime.animar()
        self.file = idleAnime.imagem