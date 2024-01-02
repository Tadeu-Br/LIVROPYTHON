f = open('compras.txt','w')
compras = ['pão','leite','manteiga','queijo']
f.write('Lista de compras\n')
for item in compras: 
    f.write('Produto:'+item+'\n')
f.close()