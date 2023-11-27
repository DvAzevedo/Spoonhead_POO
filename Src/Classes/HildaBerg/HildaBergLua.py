from tupy import*
from Classes.Animacao import Animacao
from Classes.bars_indicators import *
from Classes.Personagem import *
from Classes.HildaBerg.listasDeImagens import hildaMoon
from Classes.Hitbox import HitBox

class HildaBergLua(Personagem):
    QTD_IMAGENS = 16
    ATRASO_DE_ANIMACAO = 2
    
    def __init__(self, x: int, y: int, vida: int, hitbox: HitBox) -> None:
        super().__init__(x, y, vida, hitbox)
        self.file = hildaMoon[0]
        self.normalAnime = Animacao(HildaBergLua.QTD_IMAGENS, hildaMoon, HildaBergLua.ATRASO_DE_ANIMACAO)

    def ataca(self) -> None:
        return super().ataca()

    def movimenta(self) -> None:
        return super().movimenta()

    def update(self) -> None:
        self.normalAnime.animar()
        self.file = self.normalAnime.imagem
        self.hitbox.atualiza_posicao(self.posX - 80, self.posY - 55)