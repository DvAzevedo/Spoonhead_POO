from tupy import Image, keyboard
from Classes.personagem import Personagem
from Classes.animacao import Contador, Animate
from Classes.Hitbox import HitBox
from Classes.chaliceImgLists import *

class Chalice(Personagem):
    QTD_IMAGENS_NORMAL = 3
    QTD_IMAGENS_TRANSICAO_ESPECIAL = 18
    QTD_IMAGENS_ESPECIAL = 4

    def __init__(self, vilao, life = 3, x=240, y=240):
        super().__init__(x, y, life)
        self.k = 30
        self.atk_c = 0
        self.is_atk_possible = True
        self.c = 0
        self.vilao = vilao
        self.animate_normal = Animate(Chalice.QTD_IMAGENS_NORMAL, ChaliceNormal, 6)
        self.atacando = False
        self.hitbox = HitBox(x, y, 30, 30)
        self.animate_trasition_special = Animate(Chalice.QTD_IMAGENS_TRANSICAO_ESPECIAL, ChaliceTransitionToSpecial, 2)
        self.animacao_special = Animate(Chalice.QTD_IMAGENS_ESPECIAL, ChaliceSpecial, 3)
        self.animacao_atual = self.animate_normal

    def update(self) -> None:
        self.change_direction()
        self.common_attack()
        self.flee()
        self.file = self.animacao_atual.anima()
        if(self.file == self.animate_trasition_special.lastImg):
            self.animacao_atual = self.animacao_special
        if(self.animacao_atual == self.animacao_special and self._collides_with(self.vilao)):
            Explosao(self.x, self.y)
            self.animacao_atual = self.animate_normal
        
    def change_direction(self) -> None:
        if self.animacao_atual == self.animate_normal or self.animacao_atual == self.animacao_special:
            if keyboard.is_key_down('Left') and self.x >= 20:
                self.x -= self.k
            if keyboard.is_key_down('Right') and self.x <= 780:
                self.x += self.k
            if keyboard.is_key_down('Up') and self.y >= 20:
                self.y -= self.k
            if keyboard.is_key_down('Down') and self.y <= 480:
                self.y += self.k
        if self.animacao_atual == self.animate_normal:
            if keyboard.is_key_down('e'):
                self.atacando = False
                self.animacao_atual = self.animate_trasition_special
        self.hitbox.atualiza_posicao(self.x, self.y)

    def common_attack(self) -> None:
        if keyboard.is_key_just_down('space'):
            if(self.animacao_atual == self.animate_normal):
                self.atacando = not self.atacando
        if self.atacando == True:
            if self.atk_c % 2 == 0:
                b = Bullet(self.x,self.y + 8, self.vilao)
            else:
                b = Bullet(self.x,self.y - 8, self.vilao)
            self.atk_c += 1

    def flee(self) -> None:
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
 
class Explosao(Image):
    QTD_IMAGENS_EXPLOSAO = 27
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.animacao_explosion = Animate(Explosao.QTD_IMAGENS_EXPLOSAO, ChaliceExplosion, 1)
    def update(self):
        self.file = self.animacao_explosion.anima()
        if self.animacao_explosion.isLastImg:
            self.destroy()