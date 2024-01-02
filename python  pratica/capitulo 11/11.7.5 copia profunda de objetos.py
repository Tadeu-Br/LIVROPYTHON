import copy 
class Pessoa: 
    def __init__(self, nome, idade, valores):
        self.nome = nome 
        self.idade = idade 
        self.lista = valores 
    def __str__(self): 
        return f"Nome: {self.nome}, Idade: {self.idade}, Lista: {self.lista}" 
pessoa1 = Pessoa("João", 30, [10,20])
#aqui é a copia profunda.
pessoa2 = copy.deepcopy(pessoa1)
#que está vivo. 
pessoa1.idade = 20
pessoa1.lista[0] = 100

print(pessoa1) 
print(pessoa2) 
print(id(pessoa1)) 
print(id(pessoa2))