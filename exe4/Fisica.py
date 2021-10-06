from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nome=None, __codigo=None, __endereco=None, __telefone=None,__cpf=None,altura=None,peso=None,idade=None):
        super().__init__(nome, __codigo,__endereco, __telefone)
        self.__cpf = __cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,Cpf):
        admin =True
        if admin == True:
            self.__cpf = Cpf
        else:
            print("recurso disponivel somente para administradores")


    def imprimeCPF(self):
        super().imprimeNome()
        print("cpf:",self.cpf)
        print("idade:",self.idade)

    def __calculaIMC(self):
        super().imprimeTelefone()
        print("peso:",self.peso)
        print("altura:",self.altura)
        imc = round(self.peso / (self.altura*self.altura),2)
        print("imc:",imc)
    
    @property
    def calculaIMC(self):
        return self.__calculaIMC
