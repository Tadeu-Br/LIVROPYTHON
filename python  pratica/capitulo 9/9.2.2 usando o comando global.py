def funcao(): 
    
    #uma global diz que é determinado por completo
    #no x, que portanto, não pode ser mudado.
    global x 
    x = 20 
    print('X = ',x)

#e esse daqui não pode ser definido como 10, pois o 
# 20 está no global.
x = 10
funcao()
print('X = ',x)