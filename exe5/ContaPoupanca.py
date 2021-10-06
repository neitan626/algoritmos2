from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):

    def __init__(self,nome,numeroconta,saldo):
        self._nome = nome
        self._numeroconta = numeroconta
        self._saldo=saldo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self,valor):
        self._nome = valor

    @property
    def numeroconta(self):
        return self._numeroconta

    @numeroconta.setter
    def numeroconta (self,valor):
        self._numeroconta = valor

    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo (self,valor):
        self._saldo = valor

    def imprimir(self):
        print("Conta Poupança")
        super().imprimir()
        

    def cadastro(self):
        self.imprimir()

    def depositar(self,valor):
        self._saldo += valor
        print("Você depositou",valor,"reais")




    

    

    

    