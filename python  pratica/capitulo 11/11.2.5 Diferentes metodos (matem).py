class Matematica:
    # Método Estático 
    @staticmethod 
    def somar(x, y): 
        return x + y 
    # Método de Classe
    @classmethod 
    def multiplicar(cls, x, y): 
        return x * y 
    # Método de Instância
    def dividir(self, x, y): 
        return x / y 
    # Chamando um métodos estático
print(Matematica.somar(3, 5)) 
    # Chamando um métodos da classe 
print(Matematica.multiplicar(2, 4)) 
    # Criando um objeto da classe Matematica 
calc = Matematica()
    # Chamando o método de instância
print(calc.dividir(10, 2))