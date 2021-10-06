from Produto import Produto
from Categoria import Categoria

class Perecivel(Produto):
    def __init__(self, id, nome,cat:Categoria, preco,tempmin,tempmax):
        super().__init__(id, nome, cat, preco)
        self.tempmin = tempmin
        self.tempmax = tempmax

    def temperaturaMinima(self,valor):
        self.tempmin = valor

    def temperaturaMaxima(self,valor):
        self.tempmax = valor

    def imprimir(self):
        print("Produto Perecível")
        print("id:",self.id)
        print("nome:",self.nome)
        print("preço R$:",self.preco)
        print("categoria:",self.cat.nome)
        print("id categoria:",self.cat.id)
        print("temperatura máxima:",self.tempmax,"ºC")
        print("temperatura mínima:",self.tempmin,"ºC")
