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
        self.shooting = False
        self.y_upDo = 1
        self.count = 0
    def justShoot(self):
        if keyboard.is_key_just_down('space'):
            self.armas[0].x = self.x -20
            self.armas[0].y = self.y +(self.y_upDo*30)
            self.armas[0].atirou = True
        if keyboard.is_key_just_down('Up'):  
            self.armas[1].x = self.x -20
            self.armas[1].y = self.y +(self.y_upDo*30)
            self.armas[1].atirou = True
        if keyboard.is_key_just_down('Left'):  
            self.armas[2].x = self.x -20
            self.armas[2].y = self.y+(self.y_upDo*30)
            self.armas[2].atirou = True
        if keyboard.is_key_just_down('Right'):  
            self.armas[3].x = self.x -20
            self.armas[3].y = self.y+(self.y_upDo*30)
            self.armas[3].atirou = True
    def update(self):
        if self.y == 400 or self.y == 200:
            self.y_upDo = -(1)*self.y_upDo
        if self.count%10 == 0:
            self.y += self.y_upDo
        self.count += 0
        self.justShoot()
        for i in range(len(self.armas)):
            self.armas[i].update()