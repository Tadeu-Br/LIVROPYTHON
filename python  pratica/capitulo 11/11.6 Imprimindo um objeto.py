class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 
    def __str__(self): 
        return f"Nome: {self.nome}, Idade: {self.idade}" 

#aqui quando puxa o valor pessoa, mete dentro dela 
#as coisas que vão dentro. então, quando é feito
#em string, vai "Nome: João, Idade: 30"
pessoa = Pessoa("João", 30) 

print(pessoa)