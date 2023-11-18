from Classes.Contador import Contador

class Animacao:
    def __init__(self, qtd_imgs: int, imgs: list, atraso: int) -> None:
        self._atrasoCont = Contador(atraso)
        self._imgsCont = Contador(qtd_imgs)
        self._listaImagens = imgs
        self._imagem = imgs[0]
        self._ultimaImg = imgs[qtd_imgs-1]
        self._fim = False
        pass

    @property
    def atrasoCont(self) -> Contador:
        return self._atrasoCont
    
    @atrasoCont.setter
    def atrasoCont(self, cont: Contador) -> None:
        self._atrasoCont = cont
        pass
    
    @property
    def imgsCont(self) -> Contador:
        return self._imgsCont
    
    @imgsCont.setter
    def imgsCont(self, cont: Contador) -> None:
        self._imgsCont = cont
        pass
    
    @property
    def listaImagens(self) -> list:
        return self._listaImagens
    
    @listaImagens.setter
    def listaImagens(self, lista: list) -> None:
        self._listaImagens = lista
        pass
    
    @property
    def imagem(self) -> str:
        return self._imagem
    
    @imagem.setter
    def imagem(self, img: str) -> None:
        self._imagem = img
        pass
    
    @property
    def ultimaImg(self) -> str:
        return self._ultimaImg
    
    @ultimaImg.setter
    def ultimaImg(self, img: str) -> None:
        self._ultimaImg = img
        pass
    
    @property
    def fim(self) -> bool:
        return self._fim
    
    @fim.setter
    def fim(self, valor: bool) -> None:
        self._fim = valor
        pass
    
    def animar(self) -> None:
        self.atrasoCont.incrementa()
        if self.atrasoCont.esta_zerado():
            if self.imagem == self.ultimaImg:
                self.fim = True
            self.imagem = self.listaImagens[self.imgsCont.contador]
            self.imgsCont.incrementa()
        pass
            
    def anima(self) -> str:
        self.animar()
        if self.imagem == self.ultimaImg:
            aux = self.imagem
            self.animar()
            return aux
        return self.imagem