import math
from Classes.Ataque import *
from Classes.Chalice.listasDeImagens import MiniBombMove

class MiniBomba(Ataque):
    QTD_IMAGENS = 8
    
    def __init__(self, x: int, y: int, alvo: Personagem, angulo: int, tipoDaAnimacao: str, velocidade=25) -> None:
        self._angulo = angulo*(math.pi)/180
        self._tipoDaAnimacao = tipoDaAnimacao
        self._velocidadeX = velocidade
        self._velocidadeY = self.velocidadeX * (math.sin(self.angulo))
        super().__init__(x, y, alvo, Animacao(MiniBomba.QTD_IMAGENS, MiniBombMove, 2), 5)
        self._animacaoAtual = self.animacao
        pass
    
    @property
    def angulo(self) -> float:
        return self._angulo
    
    @angulo.setter
    def angulo(self, angulo: float) -> None:
        self._angulo = angulo
        pass
    
    @property
    def tipoDaAnimacao(self) -> str:
        return self._tipoDaAnimacao
    
    @tipoDaAnimacao.setter
    def tipoDaAnimacao(self, tipo: str) -> None:
        self._tipoDaAnimacao = tipo
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
        self.posX += 0.7 * self.velocidadeX
        self.velocidadeY -= 2
        self.posY -= self.velocidadeY
        pass
        
    def causa_dano(self) -> None:
        self.alvo.sofre_dano(self.dano)
        pass
    
    def update(self) -> None:
        self.file = self.animacaoAtual.anima()
        self.atualiza_coordenadas()