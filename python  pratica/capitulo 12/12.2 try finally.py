try:
    arquivo = open("arquivo.txt", "r") 
    conteudo = arquivo.read() 
#depois, termina com o finlally.
finally: 
    arquivo.close()
    
