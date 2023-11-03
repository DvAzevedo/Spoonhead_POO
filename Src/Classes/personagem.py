from tupy import*

class Personagem(Image):
    def __init__(self, x, y, image, life, armas):
        self.file = image[0]
        self.imgs = image
        self.x = x
        self.y = y
        self.life = life
        self.armas = armas

class Vilao_test_1(Personagem):
    def __init__(self, x, y, image, life, armas):
        super().__init__(x, y, image, life, armas)
        self.shooting = False
        self.y_upDo = 1
        self.imgChange = 1
        self.count = 0
    def justShoot(self):
        if keyboard.is_key_down('space'):
            self.armas[0].x = self.x -20
            self.armas[0].y = self.y +(self.y_upDo)
            self.armas[0].atirou = True
        if keyboard.is_key_down('Up'):  
            self.armas[1].x = self.x -20
            self.armas[1].y = self.y +(self.y_upDo)
            self.armas[1].atirou = True
        if keyboard.is_key_down('Left'):  
            self.armas[2].x = self.x -20
            self.armas[2].y = self.y+(self.y_upDo)
            self.armas[2].atirou = True
        if keyboard.is_key_down('Right'):  
            self.armas[3].x = self.x -20
            self.armas[3].y = self.y+(self.y_upDo)
            self.armas[3].atirou = True
    def update(self):
        # if self.imgChange% 100 == 0:
        #     self.file = self.imgs[1]
        
        if self.y == 400 or self.y == 100:
            if self.imgChange == 0:
                self.imgChange = 1
            else:
                self.imgChange = 0
            self.y_upDo = -(1)*self.y_upDo
            self.file = self.imgs[self.imgChange]
            
        if self.count%10 == 0:
            self.y += self.y_upDo
        self.count += 0
        self.justShoot()
        for i in range(len(self.armas)):
            self.armas[i].update()