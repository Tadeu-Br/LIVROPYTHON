A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
while A < B: 
    A = A + 1
    if (A == 5) | (A == 6) | (A == 7) | (A == 8) | (A == 9) |(A == 13):
            continue
    
    print("Valor = ",A)
print("Fim do programa")