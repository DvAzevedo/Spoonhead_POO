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
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x1):
        self._x = x1
        pass
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y1):
        self._y = y1
        pass
    
    def update(self) -> None:
        self._file = self.animacao.anima()