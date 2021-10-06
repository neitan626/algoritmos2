from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade,numMarcha,bagageiro):
        super().__init__(marca, qtdRodas, modelo,velocidade)
        self.numMarcha =numMarcha
        self.bagageiro =bagageiro
    
    def Imprimir(self):
        super().Imprimir()
        print("possui",self.numMarcha,"marchas")
        if self.bagageiro == "sim":
            print("e possui bagageiro")
        else:
            print("e não possui bagageiro")
