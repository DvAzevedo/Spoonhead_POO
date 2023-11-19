from tupy import keyboard
import math, random
from Classes.Animacao import *
from Classes.bars_indicators import *
from Classes.Chalice.Ataques.Tiro import Tiro
from Classes.Chalice.Ataques.MiniBomba import MiniBomba
from Classes.Chalice.listasDeImagens import *
from Classes.Personagem import *

class Chalice(Personagem):
    QTD_IMAGENS_NORMAL = 6
    QTD_IMAGENS_TRANSICAO_ESPECIAL = 18
    QTD_IMAGENS_ESPECIAL = 4

    def __init__(self, vilao, vida = 3, x=240, y=240):
        super().__init__(x, y, vida, HitBox(x, y, 50, 25))
        self.k = 20
        self.atk_c = 0
        self.is_atk_possible = True
        self.c = 0
        self.vilao = vilao
        self.animate_normal = Animacao(Chalice.QTD_IMAGENS_NORMAL, ChaliceNormal, 6)
        self.atacando = False
        #self.hitbox = HitBox(x, y, 30, 30)
        self.animate_trasition_special = Animacao(Chalice.QTD_IMAGENS_TRANSICAO_ESPECIAL, ChaliceTransitionToSpecial, 2)
        self.animacao_special = Animacao(Chalice.QTD_IMAGENS_ESPECIAL, ChaliceSpecial, 3)
        self.animacao_atual = self.animate_normal
        self.contador_tiro = Contador(7)
        self.contador_bomb = Contador(4)
        self.contador_test = Contador(3)
        self.contador_aux = Contador(2)
        self.contador_simple_shoot = Contador(4)
        self.aux_alternate = False
        self.attack_mode = 0
        self.especial_mode = False
        self.life = Chalice_Life_bar(vida)
        self.last_attack_object = []
        self.changed = False
    
    def update(self) -> None:
        self.change_attack_mode()
        self.common_attack_bullet()
        self.change_direction()
        self.file = self.animacao_atual.anima()
        if self.file == self.animate_trasition_special.ultimaImg:
            self.animacao_atual = self.animacao_special
        if self.animacao_atual == self.animacao_special and self._collides_with(self.vilao):
            Explosao(self.x, self.y)
            self.animacao_atual = self.animate_normal
        if keyboard.is_key_just_down('k'):
                self.life.decrease_hp()
        self.corrige_attack_em_relacao_posicao()

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
        if keyboard.is_key_just_down('z'):
            if not self.contador_aux.esta_zerado():
                self.contador_aux.zera_contador()
            if self.attack_mode == 0:
                self.attack_mode = 1
            elif self.attack_mode == 1:
                self.attack_mode = 2
            else:
                self.attack_mode = 0

    def common_attack_bullet(self) -> None:
        if keyboard.is_key_just_down('space'):
            if self.animacao_atual == self.animate_normal:
                self.atacando = not self.atacando
        if self.atacando == True:
            if self.attack_mode == 0:
                self.simple_shoot()
            if self.attack_mode == 1:
                self.triple_shoot_attack()
            if self.attack_mode == 2:
                self.mini_bomb_attack()
                self.contador_aux.zera_contador()

    def simple_shoot(self):
        # if self.contador_aux.esta_zerado():
        if self.contador_test.esta_zerado():
            if self.contador_simple_shoot.contador < 2:
                #b1 = Bullet(self.x, self.y, self.vilao, 0, 2, 0, 50, 10)
                b1 = Tiro(self.posX, self.posY, self.vilao, 0, 2, 0, 10, 50)
                self.last_attack_object.insert(0, b1)  
            else:
                #b1 = Bullet(self.x, self.y, self.vilao, 0, 2, 0, 50, -15)
                b1 = Tiro(self.posX, self.posY, self.vilao, 0, 2, 0, -15, 50)
                self.last_attack_object.insert(0, b1)  
            self.contador_simple_shoot.incrementa()
        self.contador_test.incrementa()
        # self.contador_aux.incrementa()

    def triple_shoot_attack(self):
        if self.contador_tiro.esta_zerado():
            a_disp = 8
            # b1 = Bullet(self.x,self.y , self.vilao,0,random.randrange(0,2,1),20)
            '''
            b1 = Bullet(self.x, self.y, self.vilao, 0, 2, 20)
            b2 = Bullet(self.x, self.y, self.vilao, a_disp, 0)
            b3 = Bullet(self.x, self.y, self.vilao, (-1)*a_disp, 1)
            '''
            b2 = Tiro(self.posX, self.posY, self.vilao, a_disp, 0)
            b1 = Tiro(self.posX, self.posY, self.vilao, 0, 2, 20)
            b3 = Tiro(self.posX, self.posY, self.vilao, (-1) * a_disp, 1)
        self.contador_tiro.incrementa()

    def mini_bomb_attack(self):
        if self.contador_bomb.esta_zerado():
            if self.contador_aux.contador % 2 == 0:
                #bomb1 = Mini_Bomb(self.x, self.y, self.vilao, random.randrange(-20,1,5), "A", random.randrange(25,35,5))
                bomb1 = MiniBomba(self.posX, self.posY, self.vilao, random.randrange(-20,1,5), "A", random.randrange(25,35,5))
            else:
                #bomb2 = Mini_Bomb(self.x, self.y, self.vilao, random.randrange(0,21,5), "A", random.randrange(25,45,5))
                bomb2 = MiniBomba(self.posX, self.posY, self.vilao, random.randrange(0,21,5), "A", random.randrange(25,45,5))
            self.contador_aux.incrementa()
        self.contador_bomb.incrementa()

    '''
    def corrige_attack_em_relacao_posicao(self):
        if len(self.last_attack_object) > 0:
            if self.last_attack_object[0].changed is False:
                if self.x != (self.last_attack_object[0].x + self.last_attack_object[0].desloc_x):
                    self.last_attack_object[0].x = self.x
                    self.last_attack_object[0].changed = True
                if self.y != ((self.last_attack_object[0].y + 10) or (self.last_attack_object[0].y - 15)):
                    self.last_attack_object[0].y = (self.y + self.last_attack_object[0].desloc_y)
                    self.last_attack_object[0].changed = True
                self.last_attack_object.clear()
    '''

    def corrige_attack_em_relacao_posicao(self):
        if len(self.last_attack_object) > 0:
            if self.last_attack_object[0].mudou is False:
                if self.x != (self.last_attack_object[0].posX + self.last_attack_object[0].deslocamentoX):
                    self.last_attack_object[0].posX = self.x
                    self.last_attack_object[0].mudou = True
                if self.y != ((self.last_attack_object[0].posY + 10) or (self.last_attack_object[0].posY - 15)):
                    self.last_attack_object[0].posY = (self.y + self.last_attack_object[0].deslocamentoY)
                    self.last_attack_object[0].mudou = True
                self.last_attack_object.clear()
    
    def flee(self) -> None:
        if keyboard.is_key_just_down('q'):
            self.y -= 20
    # Break temporary your character attack
    def b_atk(self,status: bool):
        self.is_atk_possible = status

    def especial_movement(self) -> None:
        self.x += self.especial_vel
    
        
'''
class Bullet(Image):
    QTD_IMAGENS_BULLET = 4

    def __init__(self, x, y, vilao, angulo, type_animation_number=0, desloc_x=0, vel_set=35, desloc_y=0):
        self.desloc_x = desloc_x
        self.desloc_y = desloc_y
        self.x = x + desloc_x
        self.y = y + desloc_y
        self.v = vel_set
        self.animation_index = type_animation_number
        self.angle2 = angulo
        self.angle_rad = self.angle2*(math.pi)/180
        self.vy = self.v * (math.sin(self.angle_rad))
        self.vilao = vilao
        self.animate_normal = Animacao(Bullet.QTD_IMAGENS_BULLET, BulletDict[self.animation_index], 1)  
        self.animacao_atual = self.animate_normal
        self.colisao_com_vilao = False
        self.changed = False

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
            self.destroy()
        self.x += self.v
        self.y -= self.vy

    def causa_dano(self, dano: int):
        if self.vilao.life > 0:
            self.vilao.life -= dano
'''
class Mini_Bomb(Image):
    QTD_IMAGENS_MINI_BOMB = 8

    def __init__(self, x, y, vilao, angulo, type_animation: str, vel_ini_y = 25):
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
        self.animate_normal = Animacao(Mini_Bomb.QTD_IMAGENS_MINI_BOMB, MiniBombMove, 2)  
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
            self.destroy()
        self.x += 0.7*self.v
        self.vy -= 2
        self.y -= self.vy

    def causa_dano(self, dano: int):
        if self.vilao.life > 0:
            self.vilao.life -= dano
 
class Explosao(Image):
    QTD_IMAGENS_EXPLOSAO = 27
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.animacao_explosion = Animacao(Explosao.QTD_IMAGENS_EXPLOSAO, ChaliceExplosion, 1)
    def update(self):
        self.file = self.animacao_explosion.anima()
        if self.animacao_explosion.fim:
            self.destroy()