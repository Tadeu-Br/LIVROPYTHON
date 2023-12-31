lista = [21, 12, 3, 44, 5]

#ordena os elementos da lista.
lista.sort() 

print(lista) 

#retira algo da lista
lista.remove(3) 

print(lista) 

#insere um valor (x) no fim de uma lista
lista.append(10) 

print(lista) 

#insere, na posição que está sendo solicitada, um valor
lista.insert(0,-1) 
print(lista)

#se for elevado o valor, vai sempre pro final
lista.insert(9, 5) 

print(lista)

#remove e retorna o elemmento da lista pop, 
# nesse exemplo
# está tirando o terceiro eleemento e metendo
# no valor x..
x = lista.pop(3)

print(lista)
print(x)