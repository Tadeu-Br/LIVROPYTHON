class Ponto: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
        #aqui vai fazer os objetos serem equalizados 
        #se os valores de dentro deles forem iguais.
    def __eq__(self, po):
        return self.x == po.x and self.y == po.y
ponto1 = Ponto(2, 3) 
ponto2 = Ponto(2, 3)

if(ponto1 == ponto2): 
    print('Objetos iguais')
else: 
    print('Objetos diferentes')