class Pessoa: 
    def __init__(self, nome, idade): 
        # Atributo público
        self.nome = nome
        # Atributo privado
        self.__idade = idade 
pessoa1 = Pessoa("João", 30)
#isso aqui é publico e vai direitinho
print(pessoa1.nome)
#aqui é um atributo privado, por causa dos
#dois underline
print(pessoa1.__idade)