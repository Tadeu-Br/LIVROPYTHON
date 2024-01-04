#abre o arquivo, em modo de escrita
f = open('compras.txt','w')
#faz uma lista (entidade lista)
compras = ['pão','leite','manteiga','queijo']
#mete o titulo da lista.
f.write('Lista de compras\n')
for item in compras: 
    #escreve e colocacada uma das partes,
    #depois apertando o enter.
    f.write('Produto:'+item+'\n')
f.close()
#então fecha o arquivo.