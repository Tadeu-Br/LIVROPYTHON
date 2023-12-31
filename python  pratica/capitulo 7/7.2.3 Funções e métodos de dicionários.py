dic = {'nome':'João','idade':30,'cidade':'Itu'} 
# Verificando se uma chave existe no dicionário
if 'idade' in dic: 
    print("Chave 'idade' encontrada!") 
    # Obtendo o número de pares chave-valor no dicionário 
    num_pares = len(dic) 
    
    print(dic.keys()) 
    print(dic.values())