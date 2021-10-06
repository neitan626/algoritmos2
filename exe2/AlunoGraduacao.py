from Aluno import Aluno

class AlunoGraduacao(Aluno):
    
    def __init__(self, nome=None, codigo=None, matricula=None,semestre=None):
        super().__init__(nome, codigo, matricula)
        self.semestre = input("digite o semestre atual do aluno: ")

    def imprimir(self):
        super().imprimir()
        print("semetre atual do aluno:",self.semestre)
