#+= c+=a equivale a c=c+a
#-= c-=a equivale a c=c-a
#*= c*=a equivale a c=c*a
#/= c/=a equivale a c=c/a
#**= c**=a equivale a c=c**a 
#//= c//=a equivale a c=c//a
#%= c%=a equivale a c=c%a

c = int(input("Enter the value of c: "))
a = int(input("Enter the value of a: "))

print("c =", c)
print("a =", a)

c += a
print(c)
c -= a
print(c)
c *= a
print(c)
c /= a
print(c)
c //= a
print(c)
c %= a
print(c)

