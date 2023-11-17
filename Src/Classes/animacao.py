from Contador import Contador
class Animacao:
    def __init__(self, qtd_imgs, imgs, delay) -> None:
        self._delayCount = Contador(delay)
        self._imgsCount = Contador(qtd_imgs)
        self.imgs = imgs
        self.file = imgs[0]
        self.lastImg = imgs[qtd_imgs-1]
        self.isLastImg = False
        pass

    @property
    def delayCount(self) -> Contador:
        return self._delayCount
    
    @delayCount.setter
    def delayCount(self, delayCount) -> None:
        self._delayCount = delayCount
        pass
    
    @property
    def imgsCount(self) -> Contador:
        return self._imgsCount
    
    @imgsCount.setter
    def imgsCount(self, imgsCount) -> None:
        self._imgsCount = imgsCount
        pass
    
    def animate(self) -> None:
        self.delayCount.incrementa()
        if self.delayCount.esta_zerado():
            if self.file == self.lastImg:
                self.isLastImg = True
            self.file = self.imgs[self.imgsCount.contador]
            self.imgsCount.incrementa()
        pass
            
    def anima(self):
        self.animate()
        if self.file == self.lastImg:
            aux = self.file
            self.animate()
            return aux
        return self.file