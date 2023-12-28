import copy 
lista = [1, 2, 3, [4, 5]] 
lista_copia = lista.copy() 
# outra possibilidade de cópia rasa 
# lista_copia = lista[:] 
print(id(lista)) 
print(id(lista_copia)) 
lista[0] = 100 
lista_copia[3][0] = 40 
print(lista) 
print(lista_copia)