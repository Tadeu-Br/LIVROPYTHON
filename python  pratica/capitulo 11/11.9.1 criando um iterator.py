class MeuIterator:
    def __init__(self, maximo): 
        self.maximo = maximo 
        self.atual = 0 
    
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.atual < self.maximo:
            resultado = self.atual 
            self.atual += 1 
            return resultado 
        else: 
            raise StopIteration
    # Usando o iterator personalizado 
meu_iterador = MeuIterator(5) 
for numero in meu_iterador: 
    print(numero)
        