try: 
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except: 
    print("Erro na leitura do arquivo.")

finally:
    arquivo.close()