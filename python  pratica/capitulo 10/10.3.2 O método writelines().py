f = open('compras.txt','w')
compras = ['pão','leite','manteiga','queijo'] 
#aqui, cada linha é cada item.
f.writelines(compras)
f.close()
