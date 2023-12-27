y = 3
z = 4

#isso parece errado, mas deveria ser um bit-by-bit
#na prática.
x = y & z 
print("Resultado &: ",x)
x = y | z 
print("Resultado |: ",x)
x = y ^ z 
print("Resultado ^: ",x)
x = ~y 
print("Resultado ~: ",x)
x = y << z 
print("Resultado <<: ",x)
x = y >> z
print("Resultado >>: ",x)