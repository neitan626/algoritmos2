class CalculaArea:

    def __init__(self):
        self.altura = 2
        self.largura = 2
        self.area = 4
        print("A área padrão do seu triangulo é 4 e possui",self.altura,"de altura e",self.largura, "de largura" )    


    def CalcularTriangulo(self):
        self.altura = int(input("digite um novo valor para a altura do triangulo:"))
     
        self.largura = int(input("digite um novo valor para a largura do triangulo:"))
        
        self.area = (self.altura * self.largura)
        return self.area

    def imprimir(self):
        print("A área do seu triangulo é:",self.area,"e possui",self.altura,"de altura e",self.largura, "de largura" )    

            