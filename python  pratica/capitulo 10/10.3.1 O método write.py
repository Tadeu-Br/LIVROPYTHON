#mesma coisa, exceto por uma parte.
f = open('compras.txt','w')
compras = ['pão','leite','manteiga','queijo'] 

f.write('Lista de compras\n')

for item in compras: 
    f.write('Produto:'+item+'\n')
#aqui puxa a quantidade.
qtd = len(compras)
#e aqui depois escreve a quantidade.
f.write('Quantidade: '+str(qtd))
f.close()