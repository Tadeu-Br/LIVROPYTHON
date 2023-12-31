# sem retorno ...
def imprime(los):
    for valor in los: 
        print(valor) 
        
lista = [1,2,3,4,5]
imprime(lista)

print("===========================")

#com retorno ...

def soma(las):
    s = 0
    for valor in las:
        s = s + valor 
    return s 
lista = [1,2,3,4,5] 
res = soma(lista)
print(res)


def soma(lis):
    s = 0 for valor in lis:
        s = s + valor 
    return s
    print('Fim da função') 
lista = [1,2,3,4,5] 
res = soma(lista)
print(res)