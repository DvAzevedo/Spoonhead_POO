from tupy import Image
from Classes.Animacao import Animacao
from Classes.Chalice.listasDeImagens import Spark

class ShootSpark(Image):
    QTD_IMAGENS = 4
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self.file = Spark[0]
        self.animacao = Animacao(ShootSpark.QTD_IMAGENS, Spark, 2)
    
    @property
    def posX(self) -> int:
        return self._x
    
    @posX.setter
    def posX(self, x1: int) -> None:
        self._x = x1
        pass
    
    @property
    def posY(self) -> int:
        return self._y
    
    @posY.setter
    def posY(self, y1: int) -> None:
        self._y = y1
        pass
    
    def update(self) -> None:
        self._file = self.animacao.anima()