def reajuste(salario,juros = 0.25):
    return salario + salario * juros
# chama a função e especifica o valor do juros 
A = reajuste(100,10)
# chama a função e usa o valor padrão do juros 

B = reajuste(100)
print(A)
print(B)