from tupy import*
from Classes.animacao import Contador

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

class HildaBergNormal(Image):
    MAX_CONTADOR_UPDATES = 21
    def __init__(self, x, y):
        self.file = hildaNormal[0]
        self.imgs = hildaNormal
        self.x = x
        self.y = y
        self._contador = Contador(HildaBergNormal.MAX_CONTADOR_UPDATES)
        self._contador_de_imagens = Contador(21)
        self.count = 0

    def update(self):
        self.count +=1
        self._contador.incrementa()
        self._file = self.imgs[self._contador_de_imagens._contador]
        self._contador_de_imagens.incrementa()
        if self.count == 100:
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
            HildaBergMoon(self.x, self.y)
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
        