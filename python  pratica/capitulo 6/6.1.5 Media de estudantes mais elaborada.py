
N = 5 # número de aluno 
notas = []
media = 0
print("Digite a nota dos alunos: ")

for i in range(N):
    x = int(input('Nota do aluno: '))
    notas.append(x)
    media = media + x
    
media = media / N
for x in notas:
    if(x > media):
        print("Aprovado: ",x)