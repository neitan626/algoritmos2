from abc import ABCMeta,abstractmethod

class ContaBancaria(metaclass=ABCMeta):

    @property
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome (self,valor):
        pass

    @property
    def numeroconta(self):
        pass

    @numeroconta.setter
    @abstractmethod
    def numeroconta (self,valor):
        pass


    @property
    def saldo(self):
        pass

    @saldo.setter
    @abstractmethod
    def saldo (self,valor):
        pass

    def imprimir(self):
        print("nome do proprietário:",self.nome)
        print("número da conta:",self.numeroconta)
        print("saldo da conta:",self.saldo)
        

    @abstractmethod
    def cadastro(self):
        pass

    @abstractmethod
    def depositar(self,valor):
        pass



    

    

    

    