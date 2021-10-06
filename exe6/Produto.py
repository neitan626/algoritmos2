from Categoria import Categoria

class Produto:
    def __init__(self,id,nome,cat:Categoria,preco):
        self.id = id
        self.nome = nome
        self.cat = cat
        self.preco = preco

    def imprimir(self):
        print("Produto não Perecível")
        print("id:",self.id)
        print("nome:",self.nome)
        print("preço R$:",self.preco)
        print("categoria:",self.cat.nome)
        print("id categoria:",self.cat.id)
        

        