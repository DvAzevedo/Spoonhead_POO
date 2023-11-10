from tupy import Rectangle

class HitBox(Rectangle):
    def __init__(self, x: int, y: int, widht: int, height: int):
        self.Hit_box = Rectangle(x, y, height, widht, outline = 'black')
        #para deixar a hitbox transparente faça outline = '', incialmente as linhas são boas para ter uma noção do tamanho
    def atualiza_posicao(self, x, y):
        self.Hit_box.x = x
        self.Hit_box.y = y