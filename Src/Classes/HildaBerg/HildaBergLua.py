
from Classes.Animacao import *
from Classes.Personagem import *
# from Classes.HildaBerg import HildaBergLua
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.trajetoria import *
from Classes.cena import cena
from Classes.bars_indicators import *

QTD_IMG_MOON_STATE_NORMAL = 16
QTD_IMG_MOON_STATE_ATK_INTRO = 12
QTD_IMG_MOON_STATE_ATK = 8
QTD_IMG_MOON_STATE_ATK_BACK = 8
QTD_IMG_MOON_STATE_SMOKE = 15
QTD_IMG_MOON_STATE_DEATH = 16
ANIME_DELAY_MOON = 2

MOON_STATE_LIST = ["idle", "atkIntro", "atk", "death"]

idleAnime = Animacao(QTD_IMG_MOON_STATE_NORMAL, hildaMoon, ANIME_DELAY_MOON)
atkIntroAnime = Animacao(QTD_IMG_MOON_STATE_ATK_INTRO, moonAtkIntro, ANIME_DELAY_MOON)
atkAnime = Animacao(QTD_IMG_MOON_STATE_ATK, moonAtk, ANIME_DELAY_MOON)
atkBackAnime = Animacao(QTD_IMG_MOON_STATE_ATK_BACK, moonAtkBack, ANIME_DELAY_MOON)
smokeAnime = Animacao(QTD_IMG_MOON_STATE_SMOKE, moonSmoke, ANIME_DELAY_MOON)
deathAnime = Animacao(QTD_IMG_MOON_STATE_DEATH, moonDeath, ANIME_DELAY_MOON)

MOON_STATE_DIC = {
    "idle": idleAnime,
    "atkIntro": atkIntroAnime,
    "atk": atkAnime,
    "atkBack": atkBackAnime,  
    "smoke": smokeAnime,
    "death": deathAnime
}

class HildaBergLua(Personagem):
    
    def __init__(self, x, y):
        super().__init__(x, y, 450, HitBox(x, y, 50, 50))
        self.state = MOON_STATE_LIST[0]
        self.file = MOON_STATE_DIC[self.state].listaImagens[0]
        self.x = x
        self.y = y
        self.count = 0

    def ataca(self):
        return super().ataca()

    def movimenta(self):
        return super().movimenta()

    def update(self):
        if self.vida > 0:
            self.file = idleAnime.anima()
        else:
            self.file = deathAnime.anima()