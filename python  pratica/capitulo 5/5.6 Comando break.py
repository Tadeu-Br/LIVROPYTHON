A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
while A < B: 
    A = A + 1 
    
    #aprendendo o comando break
    if A == B-1: 
        break 
    #que para o programa assim que 
    # algo do tipo acontece. Nesse caso,
    # apenas o for.
    print("Valor = ",A)

print("Fim do programa")