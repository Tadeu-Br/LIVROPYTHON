def fatorial(N): 
    if(N == 0): 
        # critério de parada 
        return 1 
    else: #parâmetro do fatorial sempre muda 
        return N * fatorial(N-1)

R = fatorial(5)
print(R)