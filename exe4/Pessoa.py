class Pessoa:
    def __init__(self,nome=None,__codigo=None,__endereco=None,__telefone=None):
        self.__codigo = __codigo
        self.nome = nome
        self.__endereco = __endereco
        self.__telefone = __telefone 

    @property
    def codigo(self):
        return self.__codigo

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def telefone(self):
        return self.__telefone

    @codigo.setter
    def codigo(self,cod):
        admin =True
        if admin == True:
            self.__codigo = cod
        else:
            print("recurso disponivel somente para administradores")

    
    @endereco.setter
    def endereco(self,end):
        admin =True
        if admin == True:
            self.__endereco = end
        else:
            print("recurso disponivel somente para administradores")


    @telefone.setter
    def telefone(self,tel):
        admin =True
        if admin == True:
            self.__telefone = tel
        else:
            print("recurso disponivel somente para administradores")


    def imprimeNome(self):
        print("nome:",self.nome)
        print("código:",self.codigo)

    def __imprimeTelefone(self):
        print("telefone:",self.telefone)
        print("endereço:",self.endereco)

    @property
    def imprimeTelefone(self):
        return self.__imprimeTelefone
    


