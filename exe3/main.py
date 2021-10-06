from Veiculo import Veiculo
from Automovel import Automovel
from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta

v1 = Veiculo("curumim","3","triciclo caseiro",20)

v1.Imprimir()

v1.Acelerar(10)
v1.Imprimir()
v1.Frear(15)
v1.Imprimir()

a1 = Automovel("volkswagem","4","gol",100,150)
a1.Imprimir()
a1.Frear(20)
a1.Imprimir()

c1 = Carro("ferrari","4","super gt",300,500,2)
c1.Imprimir()
c1.Acelerar(30)
c1.Imprimir()

m1 = Moto("bmw","2","sportivo",200,350,"sim")
m1.Imprimir()
m1.Frear(30)
m1.Imprimir()

b1 = Bicicleta("caloy","2","family",40,8,"não")
b1.Imprimir()
b1.Acelerar(8)
b1.Imprimir()


