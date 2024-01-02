#com recursão
def fatorial(N):
    if(N == 0):
        return 1 
    else:
        return N * fatorial(N-1)


n = int(input("entrada com recursao "))
print(fatorial(n))

    
#sem recursão


print('-----------')

def fatorial(N):
    fat = 1
    for i in range(1,N+1):
        fat = fat * i 
        return fat

N = 9

n = int(input("entrada sem recursao "))
print(fatorial(n))
