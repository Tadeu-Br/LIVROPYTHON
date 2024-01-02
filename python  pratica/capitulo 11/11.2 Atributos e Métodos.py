class Pessoa:
    # Atributo de Classe 
    especie = "Humana" 
    
    def __init__(self, nome, idade):
        # Atributos de Instância 
        self.nome = nome 
        self.idade = idade 
        # Criando um objeto da classe Pessoa 
pessoa1 = Pessoa("João", 30) 
# Acessando os atributos de instância
print(pessoa1.nome) 
print(pessoa1.idade) 
# Acessando o atributo de classe 
print(pessoa1.especie)