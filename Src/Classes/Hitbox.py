from tupy import Rectangle

class HitBox(Rectangle):
    def __init__(self, x: int, y: int, largura: int, altura: int) -> None:
        super().__init__(x, y, largura, altura, outline = 'black')
        pass
        #para deixar a hitbox transparente faça outline = '', inicialmente as linhas são boas para ter uma noção do tamanho
    
    @property
    def posX(self) -> int:
        return self._x
    
    @posX.setter
    def posX(self, x: int) -> None:
        self._x = x
    
    @property
    def posY(self) -> int:
        return self._y
    
    @posY.setter
    def posY(self, y: int) -> None:
        self._y = y
    
    def atualiza_posicao(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass
    