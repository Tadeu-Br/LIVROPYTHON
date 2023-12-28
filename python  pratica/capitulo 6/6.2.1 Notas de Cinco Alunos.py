N = 5
notas = []
for i in range(1,N+1):
    x = int(input("Nota do Aluno: "))
    notas.append(x)
    
media = 0
for n1 in notas:
    media = media + n1
media = media / N

for n1 in notas:
    if  n1 > media:
        print ("aprovado: ",n1)