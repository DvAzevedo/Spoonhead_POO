import math
from Classes.Ataque import *
from Classes.Chalice.listasDeImagens import BulletDict

class Tiro(Ataque):
    QTD_IMAGENS = 4
    
    def __init__(self, x: int, y: int, alvo: Personagem, angulo: int, indiceDaAnimacao=0, deslocamentoX=0, deslocamentoY=0, velocidade=35) -> None:
        self._angulo = angulo*(math.pi)/180
        self._indiceDaAnimacao = indiceDaAnimacao
        self._deslocamentoX = deslocamentoX
        self._deslocamentoY = deslocamentoY
        self._velocidadeX = velocidade
        self._velocidadeY = self.velocidadeX * (math.sin(self.angulo))
        super().__init__(x, y, alvo, Animacao(Tiro.QTD_IMAGENS, BulletDict[self.indiceDaAnimacao], 1), 2)
        self._animacaoAtual = self.animacao
        self.mudou = False
        pass
    
    @property
    def angulo(self) -> float:
        return self._angulo
    
    @angulo.setter
    def angulo(self, angulo: float) -> None:
        self._angulo = angulo
        pass
    
    @property
    def indiceDaAnimacao(self) -> int:
        return self._indiceDaAnimacao
    
    @indiceDaAnimacao.setter
    def indiceDaAnimacao(self, indice: int) -> None:
        self._indiceDaAnimacao = indice
        pass
    
    @property
    def deslocamentoX(self) -> int:
        return self._deslocamentoX
    
    @deslocamentoX.setter
    def deslocamentoX(self, deslocamento: int) -> None:
        self._deslocamentoX = deslocamento
        pass
    
    @property
    def deslocamentoY(self) -> int:
        return self._deslocamentoY
    
    @deslocamentoY.setter
    def deslocamentoY(self, deslocamento: int) -> None:
        self._deslocamentoY = deslocamento
        pass
    
    @property
    def velocidadeX(self) -> int:
        return self._velocidadeX
    
    @velocidadeX.setter
    def velocidadeX(self, velocidade: int) -> None:
        self._velocidadeX = velocidade
        pass
    
    @property
    def velocidadeY(self) -> float:
        return self._velocidadeY
    
    @velocidadeY.setter
    def velocidadeY(self, velocidade: float) -> None:
        self._velocidadeY = velocidade
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
        self.posX += self.velocidadeX
        self.posY -= self.velocidadeY
        pass
        
    def causa_dano(self) -> None:
        self.alvo.sofre_dano(self.dano)
        pass
    
    def update(self) -> None:
        self.file = self.animacaoAtual.anima()
        self.atualiza_coordenadas()