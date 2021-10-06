from Produto import Produto
from Perecivel import Perecivel
from Categoria import Categoria

c1 = Categoria(1,"limpeza")
c2 = Categoria(2,"frutifera")

c1.imprimir()
c2.imprimir()

print("-----------")
p1 =Produto(12,"Sabão",c1,3.99)
p1.imprimir()
print("-----------")
p2 = Perecivel(18,"Tomate",c2,7.00,8.05,17.30)
p2.imprimir()
