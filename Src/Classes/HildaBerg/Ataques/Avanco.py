from Classes.Animacao import Animacao
from Classes.Ataque import *
from Classes.HildaBerg.listasDeImagens import hildaDashIntro, hildaDash, dashSmoke, dashExplo
from Classes.HildaBerg.trajetoria import *
from Classes.HildaBerg.Ataques.EstrelaDeTouro import EstrelaDeTouro
import numpy as np

class Avanco(Ataque):
    QTD_IMGS_INTRO = 18
    QTD_IMGS_AVANCO = 6
    ATRASO_DE_ANIMACAO = 2
    
    def __init__(self, x: int, y: int, alvo: Personagem, ator: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(Avanco.QTD_IMGS_AVANCO, hildaDash, Avanco.ATRASO_DE_ANIMACAO), 1)
        self._animacaoIntro = Animacao(Avanco.QTD_IMGS_INTRO, hildaDashIntro, 1)
        self._ator = ator
        self._estrela = False
        pass
    
    @property
    def animacaoIntro(self) -> Animacao:
        return self._animacaoIntro
    
    @animacaoIntro.setter
    def animacaoIntro(self, animacao: Animacao) -> None:
        self._animacaoIntro = animacao
        pass
    
    @property
    def ator(self) -> Personagem:
        return self._ator
    
    @ator.setter
    def ator(self, ator: Personagem) -> None:
        self._ator = ator
        pass
    
    @property
    def estrela(self) -> bool:
        return self._estrela
    
    @estrela.setter
    def estrela(self, estrela: bool) -> None:
        self._estrela = estrela
        pass
    
    def atualiza_coordenadas(self) -> None:
        if self.colide_com_alvo(self.alvo):
            self.causa_dano()
        self.tipoDeAnimacao()
        pass
    
    def causa_dano(self) -> None:
        self.alvo.decrementa_vida()
        pass
    
    def tipoDeAnimacao(self) -> None:
        if self.ator.estado == "avancoIntro":
            self._hide()
            self.animacaoIntro.animar()
            self.file = self.animacaoIntro.imagem
            self.ator.file = self.file
            self.ator.volta_ao_normal(self.animacaoIntro.ultimaImg, "avanco")
            if self.ator.file == self.animacaoIntro.ultimaImg:
                Fumaca(self.ator.posX, self.ator.posY, self.alvo)
        if self.ator.estado == "avanco":
            self._hide()
            self.animacao.animar()
            self.file = self.animacao.imagem
            self.ator.file = self.file
            if self.ator.file == hildaDash[1] and not self.estrela:
                EstrelaDeTouro(self.ator.posX, self.ator.posY, self.alvo)
                self.estrela = True
            self.ator.volta_ao_normal(self.animacao.ultimaImg, "summonando")
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        if self.ator.file == self.animacao.ultimaImg:
            self.destroy()
        pass
    
class Fumaca(Ataque):
    QTD_IMAGENS = 6
    ATRASO_DE_ANIMACAO = 2
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(Fumaca.QTD_IMAGENS, dashSmoke, Fumaca.ATRASO_DE_ANIMACAO), 0)
        self.file = dashSmoke[0]
        self.posX += 190
        self.posY += 13
        pass
    
    def atualiza_coordenadas(self) -> None:
        self.posX -= 60
        pass
    
    def causa_dano(self) -> None:
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        self.file = self.animacao.anima()
        if self.file == self.animacao.ultimaImg:
            self.destroy()
        pass

class Explosao(Ataque):
    ORIGEM_X = 700
    ORIGEM_Y = 240
    QTD_IMAGENS = 15
    ATRASO_DE_ANIMACAO = 2
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(Explosao.QTD_IMAGENS, dashExplo, Explosao.ATRASO_DE_ANIMACAO), 0)
        self.file = dashExplo[0]
        self._theta = np.linspace(0, 30 * np.pi, 30)
        self._incrementador = 0
        pass
    
    @property
    def theta(self):
        return self._theta
    
    @theta.setter
    def theta(self, theta) -> None:
        self._theta = theta
        pass
    
    @property
    def incrementador(self) -> int:
        return self._incrementador
    
    @incrementador.setter
    def incrementador(self, incremento: int) -> None:
        self._incrementador = incremento
        pass
    
    def atualiza_coordenadas(self) -> None:
        coordenadas = archimedean_spiral(self.theta[self.incrementador], 1, 1)
        self.posX = coordenadas[0] + Explosao.ORIGEM_X
        self.posY = coordenadas[1] + Explosao.ORIGEM_Y
        self.incrementador += 1
        pass
    
    def causa_dano(self) -> None:
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        self.file = self.animacao.anima()
        if self.file == self.animacao.ultimaImg:
            self.destroy()
        pass
