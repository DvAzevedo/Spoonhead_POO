from tupy import BaseImage

class Contador:
    def __init__(self, maximo):
        self._maximo = maximo
        self._contador = 0

    def incrementa(self):
        self._contador += 1
        if self._contador == self._maximo:
            self._contador = 0
    
    def esta_zerado(self):
        return self._contador == 0


class Animate:
    def __init__(self, qtd_imgs, imgs, delay):
        self._delayCount = Contador(delay)
        self._imgsCount = Contador(qtd_imgs)
        self.file = imgs[0]
        self.imgs = imgs
        self.lastImg = imgs[qtd_imgs-1]
        self.isLastImg = False

    def getImgCount(self):
        return self._imgsCount._contador
    
    def animate(self):
        self._delayCount.incrementa()
        if(self._delayCount.esta_zerado()):
            if self.file == self.lastImg:
                self.isLastImg = True
            self.file = self.imgs[self._imgsCount._contador]
            self._imgsCount.incrementa()


class Animacao(BaseImage):
    def __init__(self, arquivos, intervalo):
        self._arquivos = arquivos
        self._contador = Contador(intervalo)
        self._indice = 0
        self._file = arquivos[0]
    
    def update(self):
        self._contador.incrementa()
        if self._contador.esta_zerado():
            self._indice = (self._indice + 1) % len(self._arquivos)
            self._file = self._arquivos[self._indice]
