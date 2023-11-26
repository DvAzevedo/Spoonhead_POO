from Classes.Animacao import Animacao
from Classes.Ataque import *
from Classes.Personagem import Personagem
from Classes.HildaBerg.HildaBerg import HildaBerg
from Classes.HildaBerg.listasDeImagens import hildaDashIntro, hildaDash, dashSmoke, dashExplo
from Classes.HildaBerg.trajetoria import *
from Classes.HildaBerg.Ataques.EstrelaDeTouro import EstrelaDeTouro

class Avanco(Ataque):
    QTD_IMGS_INTRO = 18
    QTD_IMGS_AVANCO = 6
    ANIME_DELAY = 2
    
    def __init__(self, x: int, y: int, alvo: Personagem, ator: HildaBerg) -> None:
        super().__init__(x, y, alvo, Animacao(Avanco.QTD_IMGS_AVANCO, hildaDash, Avanco.ANIME_DELAY), 1)
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
    def ator(self) -> HildaBerg:
        return self._ator
    
    @ator.setter
    def ator(self, ator: HildaBerg) -> None:
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
        if self.ator.state == "dashIntro":
            self.ator._hide()
            self.animacaoIntro.animar()
            self.ator.file = self.animacaoIntro.imagem
            self.ator.voltaAoNormal(self.animacaoIntro.ultimaImg, "dash")
            if self.ator.file == self.animacaoIntro.ultimaImg:
                Fumaca(self.ator.posX, self.ator.posY, self.alvo)
        if self.ator.state == "dash":
            self.animacao.animar()
            self.ator.file = self.animacao.imagem
            if self.ator.file == hildaDash[1] and not self.estrela:
                EstrelaDeTouro(self.ator.posX, self.ator.posY, self.alvo)
                self.estrela = True
            self.ator.voltaAoNormal(self.animacao.ultimaImg, "summon")
            self.ator._show()
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        pass
    
class Fumaca(Ataque):
    QTD_IMGS_FUMACA = 6
    ANIME_DELAY = 2
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(Fumaca.QTD_IMGS_FUMACA, dashSmoke, Fumaca.ANIME_DELAY), 0)
        self.posX += 190
        self.posY += 13
        self.file = dashSmoke[0]
        pass
    
    def atualiza_coordenadas(self) -> None:
        if self.file == self.animacao.ultimaImg:
            self.destroy()
            pass
        self.posX -= 60
        pass
    
    def causa_dano(self) -> None:
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        self.file = self.animacao.anima()
        pass

class Explosao(Ataque):
    POS_X_ORIGEM = 240
    POS_Y_ORIGEM = 700
    QTD_IMGS_EXPLOSAO = 15
    ANIME_DELAY = 2
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(Explosao.QTD_IMGS_EXPLOSAO, dashExplo, Explosao.ANIME_DELAY), 0)
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
        if self.file == self.animacao.ultimaImg:
            self.destroy()
            pass
        coordenadas = archimedean_spiral(self.theta[self.incrementador], 1, 1)
        self.posX = coordenadas[0] + Explosao.POS_X_ORIGEM
        self.posY = coordenadas[1] + Explosao.POS_Y_ORIGEM
        pass
    
    def causa_dano(self) -> None:
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        self.file = self.animacao.anima()
        pass
