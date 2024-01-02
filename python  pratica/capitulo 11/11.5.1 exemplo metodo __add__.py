class Ponto: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    # Sobrecarga do operador de adição
    def __add__(self, outro_ponto):
        novo_x = self.x + outro_ponto.x
        novo_y = self.y + outro_ponto.y
        return Ponto(novo_x, novo_y)
    # Criando dois objetos da classe Ponto 
    
ponto1 = Ponto(2, 3) 
ponto2 = Ponto(5, 7)
    
ponto3 = ponto1 + ponto2 
print(ponto3.x, ponto3.y)