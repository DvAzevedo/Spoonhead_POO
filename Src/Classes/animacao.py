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
