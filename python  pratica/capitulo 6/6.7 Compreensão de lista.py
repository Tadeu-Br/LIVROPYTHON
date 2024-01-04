quadrados = []
for x in range (10):
    print(quadrados)
    quadrados.append(x**2)
    
print("===============================")
print(quadrados)

numeros = [1,2,3,4,5]
#combinar as linhas em uma só.
# nova_lista = [expressão for elemento in lista if condição]
menores = [n for n in numeros if n < 4]
print("=============")
print(menores)