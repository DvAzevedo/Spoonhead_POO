from Classes.Ataque import *
from Classes.HildaBerg.listasDeImagens import hildaTornadoAtkIntro, hildaTornadoAtk

class Tornado(Ataque):
    ANIME_DELAY = 1
    QTD_IMGS_ATK_TORNADO = 16
    QTD_IMGS_ATK_TORNADO_INTRO = 12
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(Tornado.QTD_IMGS_ATK_TORNADO, hildaTornadoAtk, Tornado.ANIME_DELAY), 1)
        self._file = hildaTornadoAtkIntro[0]
        self._animacaoIntro = Animacao(Tornado.QTD_IMGS_ATK_TORNADO_INTRO, hildaTornadoAtkIntro, 2)
        self._animacaoAtual = self.animacaoIntro
        pass
    
    @property
    def file(self) -> str:
        return self._file
    
    @file.setter
    def file(self, file: str) -> None:
        self._file = file
        pass
    
    @property
    def animacaoIntro(self) -> Animacao:
        return self._animacaoIntro
    
    @animacaoIntro.setter
    def animacaoIntro(self, animacao: Animacao) -> None:
        self._animacaoIntro = animacao
        pass
    
    @property
    def animacaoAtual(self) -> Animacao:
        return self._animacaoAtual
    
    @animacaoAtual.setter
    def animacaoAtual(self, animacao: Animacao) -> None:
        self._animacaoAtual = animacao
        pass
    
    def atualiza_coordenadas(self) -> None:
        if self.fora_da_tela():
            self.destroy()
            pass
        if self.colide_com_alvo(self.alvo):
            self.causa_dano()
            self.destroy()
            pass
        if self.animacaoAtual == self.animacao:
            if self.posX > self.alvo.posX:
                self.posX -= ((self.posX - self.alvo.posX) / 30) + 10
                self.posY -= (self.posY - self.alvo.posY) / 30
                pass
            else:
                self.posX -= 5
                if self.alvo.posY > self.posY:
                    self.posY += 2
                    pass
                self.posY -= 2
                pass 
        pass
    
    def causa_dano(self) -> None:
        self.alvo.decrementa_vida()
        pass
    
    def mudaAnimacao(self) -> None:
        if self.file == self.animacaoIntro.ultimaImg:
            self.animacaoAtual = self.animacao
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        self.mudaAnimacao()
        self.file = self.animacaoAtual.anima()
        pass
    
    