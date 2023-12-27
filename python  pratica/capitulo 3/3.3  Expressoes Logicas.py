x = 5 
y = 3
r = (x > 2) and (y < x)
print("Resultado: ",r)

r = (x%2==0) and (y > 0)
print("Resultado: ",r)

r = (x > 2) or (y > x)
print("Resultado: ",r)

r = (x%2==0) or (y < 0)
print("Resultado: ",r)

r = not(x > 2)
print("Resultado: ",r)

r = not(x > 7) and (x > y)
print("Resultado: ",r)