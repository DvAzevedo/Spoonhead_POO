import math
from Classes.Ataque import *
from Classes.HildaBerg.listasDeImagens import estrelaList

class EstrelaLua(Ataque):
    ATRASO_DE_ANIMACAO = 1
    QTD_IMAGENS = 16
    
    def __init__(self, x: int, y: int, alvo: Personagem) -> None:
        super().__init__(x, y, alvo, Animacao(EstrelaLua.QTD_IMAGENS, estrelaList, EstrelaLua.ATRASO_DE_ANIMACAO), 1)
        self._file = estrelaList[0]
        self._origemY = self.posY
        self._sen = -1
        pass
    
    @property
    def file(self) -> str:
        return self._file
    
    @file.setter
    def file(self, file: str) -> None:
        self._file = file
        pass
    
    @property
    def origemY(self) -> int:
        return self._origemY
    
    @origemY.setter
    def origemY(self, origem: int) -> None:
        self._origemY = origem
        pass
    
    @property
    def sen(self) -> float:
        return self._sen
    
    @sen.setter
    def sen(self, sen: float) -> None:
        self._sen = sen
        pass
    
    def atualiza_coordenadas(self) -> None:
        if self.fora_da_tela():
            self.destroy()
            pass
        if self.colide_com_alvo(self.alvo):
            self.causa_dano()
            self.destroy()
            pass
        self.sen += 1
        self.posX -= 20
        self.posY = ((math.sin(self.sen) * 10) + self.origemY)
        pass
    
    def causa_dano(self) -> None:
        self.alvo.decrementa_vida()
        pass
    
    def update(self) -> None:
        self.atualiza_coordenadas()
        self.animacao.animar()
        self.file = self.animacao.imagem
        pass
