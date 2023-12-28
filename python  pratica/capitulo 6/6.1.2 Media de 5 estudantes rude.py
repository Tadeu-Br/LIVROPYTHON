print("Digite a nota de 5 alunos: ")
n1 = int(input('Nota do aluno 1: '))
n2 = int(input('Nota do aluno 2: '))
n3 = int(input('Nota do aluno 3: '))
n4 = int(input('Nota do aluno 4: '))
n5 = int(input('Nota do aluno 5: '))
#formação de lista
media = (n1+n2+n3+n4+n5)/5.0
#vem aqui
if(n1 > media):
    print("Aprovado: ",n1)
if(n2 > media):
    print("Aprovado: ",n2)
if(n3 > media):
    print("Aprovado: ",n3)
if(n4 > media):
    print("Aprovado: ",n4)
if(n5 > media):
    print("Aprovado: ",n5)