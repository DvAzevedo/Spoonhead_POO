import math, random
from Classes.Ataque import *
from Classes.Chalice.listasDeImagens import MiniBombMove
from Classes.Contador import Contador

class MiniBomba(Ataque):
    QTD_IMAGENS = 8
    CONTADOR = Contador(4)
    
    def __init__(self, x: int, y: int, alvo: Personagem, angulo: int, tipoDaAnimacao: str, velocidade: int = 25,personagem = None) -> None:
        super().__init__(x, y, alvo, Animacao(MiniBomba.QTD_IMAGENS, MiniBombMove, 2), 8)
        self._angulo = angulo*(math.pi)/180
        self._tipoDaAnimacao = tipoDaAnimacao
        self._velocidadeX = velocidade
        self.file = MiniBombMove[0]
        self._velocidadeY = self.velocidadeX * (math.sin(self.angulo))
        self._animacaoAtual = self.animacao
        self._hide()
        self._personagem = personagem
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
            self.animacaoAtual = self._animacaoSmoke
            pass
        self.posX += 0.7 * self.velocidadeX
        self.velocidadeY -= 2
        self.posY -= self.velocidadeY
        pass
        
    def causa_dano(self) -> None:
        self.alvo.sofre_dano(self.dano)
        pass
    
    @classmethod
    def bombardeio(cls, contadorAuxiliar: Contador, x: int, y: int, alvo: Personagem) -> None:
        if cls.CONTADOR.esta_zerado():
            if contadorAuxiliar.contador % 2 == 0:
                bomba1 = cls(x, y, alvo, random.randrange(-20,1,5), "A", random.randrange(25,35,5))
            else:
                bomba2 = cls(x, y, alvo, random.randrange(0,21,5), "A", random.randrange(25,45,5))
            contadorAuxiliar.incrementa()
        cls.CONTADOR.incrementa()
        pass
    
    def update(self) -> None:
        self._show()
        self.file = self.animacaoAtual.anima()
        if self.animacaoAtual != self._animacaoSmoke:
            self.atualiza_coordenadas()
        if(self.file == self._animacaoSmoke.ultimaImg):
                self.destroy()
        pass