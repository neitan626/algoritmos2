from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potencia,qtdPortas):
        super().__init__(marca, qtdRodas, modelo, velocidade, potencia)
        self.qtdPortas = qtdPortas

    def Imprimir(self):
        super().Imprimir()
        print(", e possui",self.qtdPortas,"portas")