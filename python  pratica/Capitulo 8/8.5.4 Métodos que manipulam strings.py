# lower(): converte a string para minúsculo;
# upper(): converte a string para maiúsculo;
# replace(ch1,ch2): troca os caracteres ch1 por ch2
# strip(): remove espaços em branco do início e final da string
# split(): separa uma string por espaços e devolve uma lista de strings
# split(ch): separa uma string usando o caractere ch e devolve uma lista de strings


#por exemplo ...
str = "Aprender Python é muito fácil" 
# aprender python é muito fácil 
print(str.lower()) 
# APRENDER PYTHON É MUITO FÁCIL
print(str.upper()) 
# ['Aprender', 'Python', 'é', 'muito', 'fácil']
print(str.split())
# Aprender-Python-é-muito-fácil
print(str.replace(' ','-'))