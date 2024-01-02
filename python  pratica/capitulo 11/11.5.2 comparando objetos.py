class Ponto: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
ponto1 = Ponto(2, 3)
ponto2 = Ponto(2, 3) 

#o operador de igualdade tá verificando
# se são os mesmos objetos, não o conteudo deles.
if(ponto1 == ponto2):
    print('Objetos iguais') 
else: 
    print('Objetos diferentes')