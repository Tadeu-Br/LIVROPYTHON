def soma(lis):
    s = 0 
    for valor in lis:
        s = s + valor
#o return faz a coisa voltar.
    return s
#E a partir daqui, mais nada.
    print (s)
    print("Fim da função")
lista = [1,2,3,4,5] 
res = soma(lista)
print(res)