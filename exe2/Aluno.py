class Aluno:

    def __init__(self,nome= None,codigo = None,matricula= None):
        self.nome = input("digite o nome do aluno: ")
        self.codigo = input("digite o código do aluno: ")
        self.matricula = input("digite o matricula do aluno: ")

    def imprimir(self):
        print("Nome do Aluno:",self.nome)
        
        print("Código do Aluno:",self.codigo)
        
        print("Matricula do Aluno:",self.matricula)




        