f = open('compras.txt','r')
str = f.readline()
print('Posição: ',f.tell())
f.close()