# usando a herança 

# classe base
class Animal: 
    def fazer_som(self): 
        return "Som genérico de animal."
    # classes derivadas 
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"
# Criando objetos das classes derivadas
animal_generico = Animal()
doguinho = Cachorro() 

print(animal_generico.fazer_som())
print(doguinho.fazer_som())

print("-----------------------")

#  sobreposição de métodos
# classe base 
class Animal: 
    def fazer_som(self):
        return "Som genérico de animal."
# classes derivadas 

class Cachorro(Animal): 
    def fazer_som(self): 
        return "Au Au!"
# Criando objetos das classes derivadas
animal_generico = Animal()
doguinho = Cachorro() 

print(animal_generico.fazer_som()), print(doguinho.fazer_som())

print("-----------------------")

# usando construtor com a herança
# classe base 
class Animal: 
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return "Som genérico de animal."
    
# classe derivada
class Cachorro(Animal):
    def __init__(self, nome, raca):
        
# Chama o construtor da classe base
        super().__init__(nome)
        self.raca = raca
    def fazer_som(self):
        return "Au Au!" 
# Criando um objeto da classe derivada
doguinho = Cachorro("Rex", "Labrador")
print(doguinho.nome)
print(doguinho.raca)
print(doguinho.fazer_som())