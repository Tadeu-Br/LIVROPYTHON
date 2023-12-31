def incrementa(lis): 
    #lis é definido antes
    
    print("depois aqui")
    print('lis = ',lis)
    lis.append(100)
    print('lis = ',lis)

print("primeiro vem aqui")
lista = [1,2,3,4,5]
#-------------------
incrementa(lista)
#-arremessado pra o def incrementa-
print("e por ultimo aqui")
print('lis = ',lista)