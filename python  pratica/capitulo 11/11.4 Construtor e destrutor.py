class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 
        print(f'Pessoa criada: {nome}')
         
# Criando um objeto da classe Pessoa e
# passando argumentos para o construtor
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

class Pessoa:
    def __init__(self, nome, idade):
        #inicializa/cria os objetoss
        self.nome = nome
        self.idade = idade 
    def __del__(self): 
        #destroi os objetos.
        print(f"Objeto {self.nome} foi removido da memória.")

def func(): 
    pessoa1 = Pessoa("João", 30)
    pessoa2 = Pessoa("Maria", 25) 
func()