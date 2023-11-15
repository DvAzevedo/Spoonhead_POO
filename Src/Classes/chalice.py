from tupy import Image, keyboard
from Classes.personagem import Personagem
from Classes.animacao import Contador, Animate
from Classes.Hitbox import HitBox
from Classes.chaliceImgLists import *
from Classes.bars_indicators import *

import math
import random

class Chalice(Personagem):
    QTD_IMAGENS_NORMAL = 6
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
        self.contador_tiro = Contador(7)
        self.contador_bomb = Contador(4)
        self.contador_aux = Contador(2)
        self.attack_mode = 0
        self.especial_mode = False
        self.life = Chalice_Life_bar(life)

    def update(self) -> None:
        self.change_direction()
        self.change_attack_mode()
        self.common_attack_bullet()
        self.flee()
        self.file = self.animacao_atual.anima()
        if(self.file == self.animate_trasition_special.lastImg):
            self.animacao_atual = self.animacao_special
        if(self.animacao_atual == self.animacao_special and self._collides_with(self.vilao)):
            Explosao(self.x, self.y)
            self.animacao_atual = self.animate_normal
        if keyboard.is_key_just_down('k'):
                self.life.decrease_hp()

    def change_direction(self) -> None:
        if self.animacao_atual == self.animate_normal or self.animacao_atual == self.animacao_special:
            if keyboard.is_key_down('Left') and self.x >= 20:
                self.x -= self.k
            if keyboard.is_key_down('Right') and self.x <= 780:
                self.x += self.k
            if keyboard.is_key_down('Up') and self.y >= 20:
                if self.especial_mode is False:
                    self.y -= self.k
            if keyboard.is_key_down('Down') and self.y <= 480:
                if self.especial_mode is False:
                    self.y += self.k
        if self.animacao_atual == self.animate_normal:
            if keyboard.is_key_down('e'):
                self.atacando = False
                self.animacao_atual = self.animate_trasition_special
        self.hitbox.atualiza_posicao(self.x, self.y)
    
    def change_attack_mode(self):
        if keyboard.is_key_down('z'):
            if self.attack_mode == 0:
                self.attack_mode = 1
            else:
                self.attack_mode = 0

    def common_attack_bullet(self) -> None:
        if keyboard.is_key_just_down('space'):
            if(self.animacao_atual == self.animate_normal):
                self.atacando = not self.atacando
        if self.atacando == True:
            if self.contador_tiro.esta_zerado():
                if self.attack_mode == 0:
                    self.triple_shoot_attack()
            if self.contador_bomb.esta_zerado():
                if self.attack_mode == 1:
                    self.contador_aux.incrementa()
                    self.mini_bomb_attack()
            self.contador_tiro.incrementa()
            self.contador_bomb.incrementa()
    
    def triple_shoot_attack(self):
        # if self.atk_c % 2 == 0:
                    #     b = Bullet(self.x,self.y + 20, self.vilao)
                    # else:
                    #     b = Bullet(self.x,self.y - 4, self.vilao)
                    # self.atk_c += 1       
        # angulo de dispersao dos projeteis -> a_disp
        a_disp = 8
        b1 = Bullet(self.x,self.y , self.vilao,0,random.randrange(0,2,1),20)
        b2 = Bullet(self.x,self.y , self.vilao,a_disp,random.randrange(0,2,1))
        b3 = Bullet(self.x,self.y , self.vilao,(-1)*a_disp,random.randrange(0,2,1))

    def mini_bomb_attack(self):
        if self.contador_aux._contador % 2 == 0:
            
            bomb1 = Mini_Bomb(self.x,self.y, self.vilao, random.randrange(-20,1,5),"A",random.randrange(25,35,5))
        else:
            bomb2 = Mini_Bomb(self.x,self.y,self.vilao, random.randrange(0,21,5),"A",random.randrange(25,45,5))


    def flee(self) -> None:
        if keyboard.is_key_just_down('q'):
            self.y -= 20
    # Break temporary your character attack
    def b_atk(self,status: bool):
        self.is_atk_possible = status

    def especial_movement(self) -> None:
        self.x += self.especial_vel
    
        
class Bullet(Image):
    QTD_IMAGENS_BULLET = 4

    def __init__(self,x,y, vilao,angulo, type_animation_number=0,deslocamento_ini=0):
        self.x = x + deslocamento_ini
        self.y = y
        self.v = 35
        self.animation_index= type_animation_number
        self.angle = angulo
        self.angle_rad = self.angle*(math.pi)/180
        self.vy = self.v * (math.sin(self.angle_rad))
        self.vilao = vilao
        self.animate_normal = Animate(Bullet.QTD_IMAGENS_BULLET, BulletDict[self.animation_index], 1)  
        self.animacao_atual = self.animate_normal
        self.colisao_com_vilao = False

    def update(self) -> None:
        self.file = self.animacao_atual.anima()
        self.atualiza_coordenadas()
        

    def atualiza_coordenadas(self):
        if self.x > 840 or (self.y < 0 or self.y > 800):
            self.destroy()
        if self._collides_with(self.vilao):
            # self.destroy()
            if self.colisao_com_vilao is False:
                self.causa_dano(2)
            self.colisao_com_vilao = True
            self._hide()
        self.x += self.v
        self.y -= self.vy

    def causa_dano(self,dano:int):
        if self.vilao.life > 0:
            self.vilao.life -= dano

class Mini_Bomb(Image):
    QTD_IMAGENS_MINI_BOMB = 8

    def __init__(self,x,y, vilao,angulo,type_animation: str,vel_ini_y = 25):
        self.x = x
        self.y = y
        # defina velocidade padrao = 25
        self.v = 25
        self.angle = angulo
        self.angle_rad = self.angle*(math.pi)/180
        # self.vx = self.v * (math.cos(self.angle_rad))
        self.vy = vel_ini_y * (math.sin(self.angle_rad))
        self.vilao = vilao
        self.type_animation = type_animation
        # self.animation_string = f"BulletMove_type{self.type_animation}"
        self.animate_normal = Animate(Mini_Bomb.QTD_IMAGENS_MINI_BOMB, MiniBombMove, 2)  
        self.animacao_atual = self.animate_normal
        self.colisao_com_vilao = False

    def update(self) -> None:
        self.file = self.animacao_atual.anima()
        self.atualiza_coordenadas()
        

    def atualiza_coordenadas(self):
        if self.x > 840 or (self.y < 0 or self.y > 800):
            self.destroy()
        if self._collides_with(self.vilao):
            # self.destroy()
            if self.colisao_com_vilao is False:
                self.causa_dano(5)
            self.colisao_com_vilao = True
            self._hide()
        self.x += 0.7*self.v
        self.vy -= 2
        self.y -= self.vy

    def causa_dano(self,dano:int):
        if self.vilao.life > 0:
            self.vilao.life -= dano
 
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