from tupy import*
import math

# class Projectile(Image):
#     def __init__(self, imgs, x = 800, y = 300):
#         self.file = imgs[0]
#         self.imgs = imgs
#         self.x = x
#         self.y = y
#         self.helperSeno = -0.2
#         self.aux_y = y
#         pass

#     def shootSeno(self, img):
#         self.file = self.imgs[img]
#         self.helper += 0.1
#         self.x -= 10
#         self.y = ((math.sin(self.helperSeno)*75)+self.aux_y)
    
#     def shootStraight(self, xSpeed, ySpeed, img):
#         self.file = self.imgs[img]
#         self.x -= xSpeed
#         self.y -= ySpeed

#     def isOutScreen(self, x, y):
#         if x < 0:
#             return True
#         if x > 780:
#             return True
#         if y > 500:
#             return True
#         if y < 0:
#             return True
#         else:
#             return False
        
#     def stopShot(self, x, y):
#         if self.isOutScreen(x, y):
#             self.destroy()

class Projectile(Image):
    def __init__(self, image, helper):
        self.file = image
        self.helper = helper
        self.fired = False
    def isOutScreen(self, x, y):
        if x < 0:
            return True
        if x > 780:
            return True
        if y > 500:
            return True
        if y < 0:
            return True
        else:
            return False
    def stopShot(self, x, y):
        if self.isOutScreen(x, y):
            self.destroy()