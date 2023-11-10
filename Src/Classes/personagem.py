from tupy import*

class Personagem(Image):
    def __init__(self, x: int, y: int, life: int):
        self.x = x
        self.y = y
        self.life = life