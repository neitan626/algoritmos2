from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

print("Pessoa")
print("")
c1 = Pessoa("neitan",626,"rua santana","0800642")

c1.imprimeNome()
c1.imprimeTelefone()
print("")
print("Pessoa Fisica")
print("")
f1 = Fisica("neitan",626,"rua santana","0800642","859865",1.77,60,20)


f1.imprimeCPF()
f1.calculaIMC()
print("")
print("Pessoa Juridica")
print("")
j1 = Juridica("neitan",626,"rua santana","0800642",85648,984980,50)

j1.imprimeCNPJ()
j1.emitirNotaFiscal()







