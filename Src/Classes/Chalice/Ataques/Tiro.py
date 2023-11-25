import math
from Classes.Ataque import *
from Classes.Chalice.listasDeImagens import BulletDict
from Classes.Contador import Contador

class Tiro(Ataque):
    CONTADOR_TIRO_SIMPLES = Contador(3)
    CONTADOR_TIRO_TRIPLO = Contador(7)
    QTD_IMAGENS = 4
    TIROS_DISPARADOS = []
    
    def __init__(self, x: int, y: int, alvo: Personagem, angulo: int, indiceDaAnimacao: int = 0, deslocamentoX: int = 0, deslocamentoY: int = 0, velocidade: int = 35) -> None:
        self._angulo = angulo*(math.pi)/180
        self._indiceDaAnimacao = indiceDaAnimacao
        self._deslocamentoX = deslocamentoX
        self._deslocamentoY = deslocamentoY
        self._velocidadeX = velocidade
        super().__init__(x, y, alvo, Animacao(Tiro.QTD_IMAGENS, BulletDict[self.indiceDaAnimacao], 1), 2)
        self._velocidadeY = self.velocidadeX * (math.sin(self.angulo))
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
    def velocidadeY(self, velocidade: int) -> None:
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
        self.posX += self.velocidadeX
        self.posY -= self.velocidadeY
        pass
        
    def causa_dano(self) -> None:
        self.alvo.sofre_dano(self.dano)
        pass
    
    @classmethod
    def tiro_simples(cls, contadorAuxiliar: Contador, x: int, y: int, alvo: Personagem) -> None:
        if cls.CONTADOR_TIRO_SIMPLES.esta_zerado():
            if contadorAuxiliar.contador < 2:
                tiro1 = cls(x, y, alvo, 0, 2, 0, 10, 50)
                cls.TIROS_DISPARADOS.insert(0, tiro1)
            else:
                tiro2 = cls(x, y, alvo, 0, 2, 0, -15, 50)
                cls.TIROS_DISPARADOS.insert(0, tiro2)
            contadorAuxiliar.incrementa()
        cls.CONTADOR_TIRO_SIMPLES.incrementa()
        pass
    
    @classmethod
    def tiro_triplo(cls, x: int, y: int, alvo: Personagem) -> None:
        if cls.CONTADOR_TIRO_TRIPLO.esta_zerado():
            tiro1 = cls(x, y, alvo, 8)
            tiro2 = cls(x, y, alvo, 0, 2, 20)
            tiro3 = cls(x, y, alvo, -8, 1)
        cls.CONTADOR_TIRO_TRIPLO.incrementa()
        pass
    
    @classmethod
    def corrige_origem(cls, x: int, y: int) -> None:
        if len(cls.TIROS_DISPARADOS) > 0:
            if cls.TIROS_DISPARADOS[0].mudou is False:
                if x != (cls.TIROS_DISPARADOS[0].posX + cls.TIROS_DISPARADOS[0].deslocamentoX):
                    cls.TIROS_DISPARADOS[0].posX = x
                    cls.TIROS_DISPARADOS[0].mudou = True
                if y != (cls.TIROS_DISPARADOS[0].posY + 10) or y != (cls.TIROS_DISPARADOS[0].posY - 15):
                    cls.TIROS_DISPARADOS[0].posY = y + cls.TIROS_DISPARADOS[0].deslocamentoY
                    cls.TIROS_DISPARADOS[0].mudou = True
                cls.TIROS_DISPARADOS.clear()
        pass
    
    def update(self) -> None:
        self.file = self.animacaoAtual.anima()
        if self.animacaoAtual != self._animacaoSmoke:
            self.atualiza_coordenadas()
        if(self.file == self._animacaoSmoke.ultimaImg):
                self.destroy()
        pass