lista = [1, 2, 3, 4, 5]

#tem o mesmo id por serem o mesmo treco.
lista_copia = lista

#elas tem o mesmo id.
print(id(lista))
print(id(lista_copia))
#ta bao?

lista[0] = 100

print(lista)
print(lista_copia)