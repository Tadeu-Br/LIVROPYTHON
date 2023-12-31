#tuplas podem ser criadas com parenteses ou
#sem parenteses.

tupla1 = (1, 2 ,3 ,4 ,5)
tupla2 = 6, 7, 8, 9, 10
print(tupla1, tupla2)
#mas se quer uma vazia, tem que ser sem parenteses.
tuplavazia = ()

print(tuplavazia, "oi")
#tuplas com apenas um elemento devem possuir uma virgula
#pra serem consideradas elemetos, se não, serão conside
#radas tuplas.

tupla1elem = (5, )

print(tupla1elem)

#alem disso, tipos diferentes são permitidos.

tupladiff1 = (1, 2, 3, 4, 5)
tupladiff2 = (tupla1,'abc',6, 7.5)
print(tupladiff1, tupladiff2)
#ou unir tuplas
tupla3 = tupla1 + tupla2
print(tupla3)
tupla4 = 2 * tupla2
print(tupla4)