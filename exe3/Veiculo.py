
class Veiculo:

    def __init__(self,marca=None,qtdRodas=None,modelo=None,velocidade=0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def Imprimir(self):
        print("A marca do seu veiculo é",self.marca,", a quantidade de rodas é",self.qtdRodas,", o seu modelo é",self.modelo,", e a velocidade é",self.velocidade)

    def Acelerar(self,acelerando):
        self.velocidade += acelerando
    
    def Frear(self,parando):
        self.velocidade -= parando

 