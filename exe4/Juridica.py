from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nome=None, __codigo=None, __endereco=None, __telefone=None,__cnpj=None,__inscricaoEstadual=None,quantidadeFuncionarios=None):
        super().__init__(nome, __codigo, __endereco,__telefone)
        self.__cnpj = __cnpj
        self.__inscricaoEstadual = __inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    
    @property
    def cnpj(self):
        return self.__cnpj


    @cnpj.setter
    def cnpj(self,Cnpj):
        admin = True
        if admin == True:
            self.__cnpj = Cnpj
        else:
            print("recurso disponivel somente para administradores")

    @property
    def inscricaoEstadual(self):
        return self.__inscricaoEstadual


    @inscricaoEstadual.setter
    def inscricaoEstadual(self,insE):
        admin = True
        if admin == True:
            self.__inscricaoEstadual = insE
        else:
            print("recurso disponivel somente para administradores")


    def imprimeCNPJ(self):
        super().imprimeNome()
        print("cnpj:",self.cnpj)


    def __emitirNotaFiscal(self):
        super().imprimeTelefone()
        print("inscrição estadual:",self.inscricaoEstadual)
        print("quantidade de funcionarios:",self.quantidadeFuncionarios)

    @property
    def emitirNotaFiscal(self):
        return self.__emitirNotaFiscal

