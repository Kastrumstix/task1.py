#g = int(input("ведите число от 3 до 20: ",))
mass = []
import random
g = random.randint(3, 20)
print(g)
for i in range(1, g+1):
    for j in range(1, i+1):
        if (i+j) == g or ( g % (i+j) == 0 and j != 0):
            mass.append(j)
            mass.append(i)


print(mass)
