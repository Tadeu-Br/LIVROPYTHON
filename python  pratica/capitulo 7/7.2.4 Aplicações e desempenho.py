# Armazenando configurações de um programa de forma organizada 
configuracoes = { 'tamanho_fonte': 17, 'cor_fundo': 'roxo', 'modo_noturno': False }
# Contagem de frequência de letras 
texto = "abracadabra" 
frequencia = {} 
for letra in texto: 
    if letra in frequencia: 
        frequencia[letra] += 1 
    else: frequencia[letra] = 1
    
print(frequencia)