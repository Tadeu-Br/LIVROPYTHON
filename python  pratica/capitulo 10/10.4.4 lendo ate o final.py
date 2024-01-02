f = open('compras.txt','r')

#enquanto é verdade que as linha existem,
# fica lendo as linhas.
while True:
    str = f.readline()
    if(str == ''): 
        break 
    print(str)