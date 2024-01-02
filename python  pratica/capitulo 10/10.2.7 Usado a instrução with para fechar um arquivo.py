#abrindo e lendo em modo de leitura
with open("compras.txt", "r") as f: 
    #o str-f-read tá puxando isso.
    str = f.read() 
    print(str)