f = open('compras.txt','r')

str = f.read(5)
#procura 5 caracteres e retorna eles.
print(str)

str = f.read(5)
#mesma coisa, note que 
# elas contam barras de espaço
# como caracteres.
print(str)
f.close()