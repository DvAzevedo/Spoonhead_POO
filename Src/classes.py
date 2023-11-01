from tupy import*
import math

        
class Projetil(Image):
    def __init__(self, x, y, image, helper):
        self.file = image
        self.x = x 
        self.y = y
        self.helper = helper
        self.noAr = False
    def isOutScreen(self):
        if self.x < 0:
            return True
        if self.x > 800:
            return True
        if self.y > 500:
            return True
        if self.y < 0:
            return True
        else:
            return False
    def stopShoot(self):
        if self.isOutScreen():
            self.destroy()

        
class PedraSeno(Projetil):
    def __init__(self, noAr = False):
        super().__init__(800, 250, "../Img/pedra_poo.png", -0.2)
        self.noAr = noAr
    def shootSeno(super):
        super.helper += 0.1
        super.x -= 10
        super.y = ((math.sin(super.helper)*250) + 250)
    def update(self):
        if self.noAr == True:
            self._show()
            self.shootSeno()
            super().stopShoot()
        else:
            self._hide()

class FogoReto(Projetil):
    def __init__(self, noAr = False):
        super().__init__(800, 250, "../Img/fogo_poo.png", -0.2)
        self.noAr = noAr
    def shootReto(super):
        super.x -=20
    def update(self):
        if self.noAr == True:
            self._show()
            self.shootReto()
            super().stopShoot()
        else:
            self._hide()

    

class Arma():
    def __init__(self, qtd_municao, projetil):
        self.projetil = projetil
        self.qtd_municao = qtd_municao
        self.projetilsDisparados = 0
        self.atirou = False
        self.municoes = []
        for i in range(qtd_municao):
            x = projetil()
            self.municoes.append(x)
        self.currentMuni = [0]
    def reloadMuni(self):
        self.municoes.clear()
        for i in range(self.qtd_municao):
            x = self.projetil()
            self.municoes.append(x)
        self.currentMuni = [0]
    def shoot(self):
        if self.projetilsDisparados < self.qtd_municao:
            print("pD < m")
            self.municoes[self.projetilsDisparados].noAr = True
            self.projetilsDisparados += 1
        else:
            print('pd>')
            self.atirou = False
            self.projetilsDisparados = 0
            self.reloadMuni()
    def update(self):
        if self.atirou == True:
            self.shoot()

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

pedra = Arma(20, PedraSeno)
fogo = Arma(1, FogoReto)

vi = Vilao_test_1(800, 300, "../Img/balaoVerde_poo.webp", 200, [pedra, fogo])
run(globals())


