from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self,nome=None,codigo=None,matricula=None,ano=None):
        super().__init__(nome,codigo,matricula)
        self.ano = input("digite o ano atual do aluno: ")

    def imprimir(self):
        super().imprimir()
        print("Ano atual do aluno:",self.ano)
        