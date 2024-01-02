def fibo(n):
    if(n == 0 or n == 1):
        return n
    else:
        A = 0
        B = 1
        cont = 1
        while(cont < n): 
            C = A + B
            cont = cont + 1
            A = B
            B = C
            return C

n = int(input("entrada"))
print(fibo(n))