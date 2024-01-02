# classe base 
class Animal: 
    #aqui está inicializando.
    def __init__(self, nome):
        self.nome = nome 
        def fazer_som(self): 
            pass 
# classes derivadas 
class Cachorro(Animal): 
    #depois mete as coisas, quando ficar pedindo
    #pelo fazer som, vai passar o auau.
    def fazer_som(self):
        return "Au Au!" 

class Gato(Animal): 
    #aqui, vai perguntar o que retorna pra o gato
    #quando pedir o som, e vai retornar o miaumiau
    def fazer_som(self): 
        return "Miau!" 
# Criando objetos das classes derivadas
doguinho = Cachorro("Rex")
gatinho = Gato("Mimi")

#então, puxa aqui.
print(doguinho.nome)
print(doguinho.fazer_som())
print(gatinho.nome) 
print(gatinho.fazer_som())