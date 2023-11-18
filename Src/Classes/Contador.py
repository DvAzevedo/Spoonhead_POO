class Contador:
    def __init__(self, maximo) -> None:
        self._maximo = maximo
        self._contador = 0
        pass

    @property
    def maximo(self) -> int:
        return self._maximo
    
    @maximo.setter
    def maximo(self, maximo) -> None:
        self._maximo = maximo
        pass
    
    @property
    def contador(self) -> int:
        return self._contador
    
    @contador.setter
    def contador(self, contador) -> None:
        self._contador = contador
        pass
    
    def esta_zerado(self) -> bool:
        return self.contador == 0
    
    def incrementa(self) -> None:
        self.contador += 1
        if self.contador == self.maximo:
            self.zera_contador()
        pass
    
    def zera_contador(self) -> None:
        self.contador = 0
        pass