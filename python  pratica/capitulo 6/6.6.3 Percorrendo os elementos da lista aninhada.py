lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# Percorre apenas os elementos 
for lista in lista_aninhada: 
    for item in lista: 
        print(item) 
        
        
# Percorre os índices e elementos 
for y in range(len(lista_aninhada)): 
    for x in range(len(lista_aninhada[y])):
        print(y,x,lista_aninhada[y][x])