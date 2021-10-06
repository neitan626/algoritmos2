from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca= None, qtdRodas= None, modelo= None, velocidade= None,potencia= None):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.potencia = potencia

    def Imprimir(self):
        super().Imprimir()
        print(", e sua possui é de",self.potencia,"cavalos de potencia")
