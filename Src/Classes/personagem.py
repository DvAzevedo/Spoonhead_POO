from tupy import*

class Personagem(Image):
    def __init__(self, x, y, image, life, armas):
        self.file = image
        self.x = x
        self.y = y
        self.life = life
        self.armas = armas

class Vilao_test_1(Personagem):
    def __init__(self, x, y, image, life, armas):
        super().__init__(x, y, image, life, armas)
        self.atirando = False
        self.armas = armas
    def justShoot(self):
        if keyboard.is_key_just_down('space'):
            self.armas[0].atirou = True
        if keyboard.is_key_just_down('Up'):  
            self.armas[1].atirou = True
    def update(self):
        self.justShoot()
        for i in range(len(self.armas)):
            self.armas[i].update()