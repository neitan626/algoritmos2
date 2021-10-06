class Categoria:

    def __init__(self,id,nome):
        self.id = id
        self.nome = nome

    def imprimir(self):
        print("--Categoria--")
        print("id categoria:",self.id)
        print("nome categoria:",self.nome)
        