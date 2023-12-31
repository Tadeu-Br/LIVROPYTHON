# %c caractere
# %s string 
# %d valor inteiro 
# %u valor ineiro sem sinal 
# %f valor real (ponto flutuante) 
# %.Nf valor real (ponto flutuante) com N casas decimais 
# %% símbolo de %

reajuste = 10
inflacao = 12.5
str = "O reajuste foi de %d %% e a inflação de %2.f %%" % (reajuste,inflacao) 
print(str)