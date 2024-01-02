f = open('compras.txt','r')

# pula 20 bytes a partir do início do arquivo 
f.seek(20) 

#imprime a posição atual 
print('Posição: ',f.tell()) 

str = f.readline() 
print('Lido: ',str)
 
f.close()