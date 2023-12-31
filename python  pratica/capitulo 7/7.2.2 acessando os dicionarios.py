# Cria um dicionário 
dic = {'nome':'João','idade':30,'cidade':'Itu'} 
# Acessando um valor no dicionário 
print(dic['nome']) 
# Modificando um valor no dicionário 
dic['idade'] = 35 
# Adicionando um novo par chave-valor 
dic['profissão'] = 'Engenheiro'

print(dic)
print("===============================================")
print("===============================================")
print("===============================================")
# Iterando nas chaves do dicionário 
for chave in dic: 
    print(chave)
# Iterando nos valores do dicionário 
for valor in dic.values(): 
    print(valor) 
# Iterando nos pares chave-valor do dicionário 
for chave, valor in dic.items():
    print(f'{chave}: {valor}')