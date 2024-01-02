def fatorial(N):
    if(N == 0): 
        return 1 
    else: 
        return N * fatorial(N-1)
numero = 7
fatorial = fatorial(numero)
print(fatorial)