from tupy import*
import math
from Classes.animacao import Contador

hildaIntro = ["../../Img/HildaNormal/Intro/blimp_intro_0001.png"]
for i in range(2, 44):
    hildaIntro.append(f"../../Img/HildaNormal/Intro/blimp_intro_{i:04d}.png")

hildaNormal = ["../../Img/HildaNormal/Idle/blimp_idle_0001.png"]
for i in range(2, 22):
    hildaNormal.append(f"../../Img/HildaNormal/Idle/blimp_idle_{i:04d}.png")

hildaTransition = ["../../Img/HildaNormal/TransitionToMoon/Start/blimp_morph_0001.png"]
for i in range(2, 8):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/BoilA/blimp_morph_{i:04d}.png")
for i in range(8, 10):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/Middle/blimp_morph_{i:04d}.png")
for i in range(10, 14):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/BoilB/blimp_morph_{i:04d}.png")
for i in range(14, 49):
    hildaTransition.append(f"../../Img/HildaNormal/TransitionToMoon/End/blimp_morph_{i:04d}.png")

hildaMoon = ["../../Img/HildaMoon/Idle/blimp_moon_idle_0001.png"]
for i in range(2, 17):
    hildaMoon.append(f"../../Img/HildaMoon/Idle/blimp_moon_idle_{i:04d}.png")

hildaStates = [hildaNormal, hildaTransition, hildaMoon]

a = 100
#t = [i/100 for i in range(0, 628)]  # t varia de 0 a 2*pi em pequenos incrementos

#y = [a * math.sqrt(2) * math.cos(i) * math.sin(i) / (1 + math.sin(i)**2) for i in t]
#x = [-a * math.sqrt(2) * math.cos(i) / (1 + math.sin(i)**2) for i in t]
class Animate:
    def __init__(self, maxUpdates, imgs):
        self._contador = Contador(maxUpdates)
        self._contador_de_imagens = Contador(maxUpdates)
        self.file = imgs[0]
        self.imgs = imgs
    def animate(self):
        self._contador.incrementa()
        self.file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        

class HildaBergNormal(Image):
    MAX_CONTADOR_UPDATES = 21
    MAX_CONTADOR_INTRO_UPDATES = 43
    def __init__(self, x, y):
        self.file = hildaIntro[0]
        self.estados = ["intro", "normal"]
        self.estado = self.estados[0]
        self.animateIntro = Animate(HildaBergNormal.MAX_CONTADOR_INTRO_UPDATES, hildaIntro)
        self.animateNormal = Animate(HildaBergNormal.MAX_CONTADOR_UPDATES, hildaNormal)
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(21)
        self.count = 0
        self.i = 1.5
        
    def updatePosition(self):
        self.i += 0.1
        self.x = (a * math.sqrt(2) * math.cos(self.i) * math.sin(self.i) / (1 + math.sin(self.i)**2)) +700
        self.y = (-a * math.sqrt(2) * math.cos(self.i) / (1 + math.sin(self.i)**2)) + 200

    def animate(self):
        if self.estado == "normal":
            self.animateNormal.animate()
            self.file = self.animateNormal.file
        elif self.estado == "intro":
            self.animateIntro.animate()
            self.file = self.animateIntro.file
            if self.count == 43:
                self.estado = "normal"
    def update(self):
        self.count +=1
        self.animate()
        if self.estado == "normal":
            self.updatePosition()

        if self.count == 500:
            self._hide()
            HildaBergNormalT(self.x, self.y)
            self.destroy()

class HildaBergNormalT(Image):
    MAX_CONTADOR_UPDATES = 48
    STATE = 0
    def __init__(self, x, y):
        self.file = hildaTransition[0]
        self.imgs = hildaTransition
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergNormalT.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(48)
        self.count = 0
    def update(self):
        self.count += 1
        self._contador.incrementa()
        self._file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        if self.count == 48:
            self._hide()
            HildaBergMoon(700, 220)
            self.destroy()

class HildaBergMoon(Image):
    MAX_CONTADOR_UPDATES = 16
    STATE = 0
    def __init__(self, x, y):
        self.file = hildaMoon[0]
        self.imgs = hildaMoon
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergMoon.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(16)
        self.count = 0
    def update(self):

        self._contador.incrementa()
        self._file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        self.count +=1
        if self.count == 50:
            self.destroy()



    # def changeImg(self):
    #     if keyboard.is_key_just_down('Space'):
    #         self.currentState += 1
    #         self.file = hildaStates[self.currentState][0]
    #         self.imgs = hildaStates[self.currentState]
    #         self._contador = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES[self.currentState])
    #         self._contador_de_imagens = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES[self.currentState])
# class HildaBergNormal(Image):
#     MAX_CONTADOR_UPDATES = [21, 48, 16]
#     STATE = 0
#     def __init__(self, x, y):
#         self.file = hildaStates[0][0]
#         self.imgs = hildaStates[0]
#         self.x = x
#         self.y = y
#         self._contador = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES[0])
#         self._contador_de_imagens = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES[0])
#         self.currentState = 0
#     def changeImg(self):
#         if keyboard.is_key_just_down('Space'):
#             self.currentState += 1
#             self.file = hildaStates[self.currentState][0]
#             self.imgs = hildaStates[self.currentState]
#             self._contador = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES[self.currentState])
#             self._contador_de_imagens = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES[self.currentState])
#     def update(self):
#         self.changeImg()

#         self._contador.incrementa()
#         self._file = self.imgs[self._contador_de_imagens._contador]
#         self._contador_de_imagens.incrementa()
        