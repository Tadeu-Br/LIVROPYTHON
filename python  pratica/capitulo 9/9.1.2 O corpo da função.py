def somaN(N):
# declara uma variável 
    S = 0 
# executa uma repetição 
    for i in range(1,N+1): 
        S = S + i
    # retorna o resultado 
        return S 

print(somaN(5))