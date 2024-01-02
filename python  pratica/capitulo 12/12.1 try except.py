try:
# Código que pode causar exceções 
# Tentando dividir por zero 
    resultado = 10 / 0 
except ZeroDivisionError: 
    print("Erro: Divisão por zero!")
    
try: 
    arquivo = open("arquivo.txt", "r") 
    conteudo = arquivo.read() 
    arquivo.close() 
except FileNotFoundError: 
    print("Erro: O arquivo não foi encontrado.") 
except IOError: 
    print("Erro: Ocorreu um erro de E/S.")