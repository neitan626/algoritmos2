from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

cc = ContaCorrente("neitan",181626,1000)
print("---------------")
cc.cadastro()
print("---------------")
cc.depositar(100)
print("---------------")
cc.cadastro()
print("---------------")

cp = ContaPoupanca("jair",299302    ,5000)
cp.cadastro()
print("---------------")
cp.depositar(300)
print("---------------")
cp.cadastro()
print("---------------")
