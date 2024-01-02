# classes bases 
class Animal: 
    def __init__(self, nome):
        self.nome = nome 
    def fazer_som(self):
        pass
    
class Voador:
    def voar(self):
         return "Estou voando!"
    
# classe derivada
class Pato(Animal, Voador):
    def fazer_som(self):
        return "Quack!" 
# Criando um objeto da classe Pato
pato = Pato("Donald") 

print(pato.nome) 
print(pato.fazer_som())
print(pato.voar())