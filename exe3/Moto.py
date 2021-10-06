from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potencia,partidaEletrica):
        super().__init__(marca, qtdRodas, modelo, velocidade, potencia)
        self.partidaEletrica = partidaEletrica

    
    def Imprimir(self):
        super().Imprimir()
        if self.partidaEletrica == "sim":
            print("e possui partida elétrica")
        else:
            print("e não possui partida elétrica")   