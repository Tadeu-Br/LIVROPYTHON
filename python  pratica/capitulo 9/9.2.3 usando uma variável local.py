def funcao():
    #a variavel local só pode ser acessada dentro da funcao
    #e nao fora dela. como por exemplo ...
    y = 20 
    #aqui é 20
    print('Y = ',y)

funcao()
#e aqui dá um erro, porque a funcao nao é definida.
print('Y = ',y)