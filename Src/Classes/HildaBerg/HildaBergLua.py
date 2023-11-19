from tupy import*
from Classes.Animacao import Animacao
from Classes.Personagem import Personagem
from Classes.HildaBerg.listasDeImagens import *
from Classes.HildaBerg.trajetoria import *
from Classes.bars_indicators import *

class HildaBergLua(Personagem):
    QTD_IMG_STATE_NORMAL = 16
    ANIME_DELAY = 2
    STATE = 0
    def __init__(self, x, y):
        self.file = hildaMoon[0]
        self.imgs = hildaMoon
        self.x = x
        self.y = y
        self.normalAnime = Animacao(HildaBergLua.QTD_IMG_STATE_NORMAL, hildaMoon, HildaBergLua.ANIME_DELAY)
        self.count = 0

    def update(self):
        self.normalAnime.animar()
        self.file = self.normalAnime.imagem