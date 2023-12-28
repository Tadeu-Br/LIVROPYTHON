N = int(input("Digite N:"))
fat = 1
i = 1 
#observe bem o while, ele fica repitindo tal qual
#como um for.
while (i <= N): 
    fat = fat * i 
    i = i + 1 
    print("Fatorial: ",fat)