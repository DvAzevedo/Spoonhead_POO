from tupy import*

class Personagem(Image):
    def __init__(self, x, y, image, life, armas):
        self.file = image[0]
        self.imgs = image
        self.x = x
        self.y = y
        self.life = life
        self.armas = armas

class Heroi_test_1(Personagem):
    def __init__(self, image, vilao, armas = None, life = 3, x=240, y=240):
        super().__init__(x, y, image, life, armas)
        self.k = 30
        self.atk_c = 0
        self.is_atk_possible = True
        self.c = 0
        self.vilao = vilao
        
    def update(self) -> None:
        self.change_direction()
        self.common_attack()
        self.flee()

    def change_direction(self):
        if keyboard.is_key_just_down('Left'):
            self.x -= self.k
        if keyboard.is_key_just_down('Right'):
            self.x += self.k
        if keyboard.is_key_just_down('Up'):
            self.y -= self.k
        if keyboard.is_key_just_down('Down'):
            self.y += self.k

    def common_attack(self):
        if keyboard.is_key_just_down('space'):
            if self.atk_c % 2 == 0:
                b = Bullet(self.x,self.y + 8, self.vilao)
            else:
                b = Bullet(self.x,self.y - 8, self.vilao)
            self.atk_c += 1

    def flee(self):
        if keyboard.is_key_just_down('q'):
            self.y -= 20
    # Break temporary your character attack
    def b_atk(self,status: bool):
        self.is_atk_possible = status
        
class Bullet(Image):

    def __init__(self,x,y, vilao):
        self.x = x
        self.y = y
        self.file = "../Img/Bullet.png"
        self.v = 25
        self.vilao = vilao

    def update(self) -> None:
        self.x += self.v
        if self.x > 840:
            self.destroy()
        if self._collides_with(self.vilao):
            self.destroy()

class Vilao_test_1(Personagem):
    def __init__(self, x, y, image, life, armas):
        super().__init__(x, y, image, life, armas)
        self.shooting = False
        self.y_upDo = 1
        self.imgChange = 1
        self.count = 0
    def justShoot(self):
        if keyboard.is_key_down('q'):
            self.armas[0].x = self.x -20
            self.armas[0].y = self.y +(self.y_upDo)
            self.armas[0].atirou = True
        if keyboard.is_key_down('q'):  
            self.armas[1].x = self.x -20
            self.armas[1].y = self.y +(self.y_upDo)
            self.armas[1].atirou = True
        if keyboard.is_key_down('q'):  
            self.armas[2].x = self.x -20
            self.armas[2].y = self.y+(self.y_upDo)
            self.armas[2].atirou = True
        if keyboard.is_key_down('q'):  
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