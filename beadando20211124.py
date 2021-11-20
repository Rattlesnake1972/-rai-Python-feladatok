import random

# A tömb feltöltve véletlen számokkal.

randomNums = []

for i in range(10):
    randomNums.append(random.randint(0, 100))

# A tömb elemeinek kiíratása.

for num in randomNums:
    print(num)

# Számok átlaga (average).

average = 0

for num in randomNums:
    average += num

print("A tömbben szereplő elemek átlaga: {0}".format(average / len(randomNums)))

# A tömb legkisebb (smallest) eleme.

smallest = randomNums[0]

for num in randomNums:
    if smallest > num:
        smallest = num

print("A tömbben szereplő számok legkisebb eleme: {0}".format(smallest))

# A tömb legnagyobb (biggest) eleme.

biggest = randomNums[0]

for num in randomNums:
    if biggest < num:
        biggest = num

print("A tömbben szereplő számok legnagyobb eleme: {0}".format(biggest))

# Van-e a tömbben páros szám?

van = False

for num in randomNums:
    if num % 2 == 0:
        van = True

if van == True:
    print("A tömb tartalmaz páros számot!")
else: 
    print("A tömb nem tartalmaz páros számot!")

# A tömbben szerepklő, ötvennél nagyobb számok összege.

auxvar = 0           # auxiliary variable = segédváltozó

for num in randomNums:
    if num > 50:
        auxvar += num

print("A tömbben szereplő, 50-nél nagyobb számok összege: {0}".format(auxvar))

# Hány darab 9-es van a tömbben?

auxvar = 0

for num in randomNums:
    if num == 9:
        auxvar += 1

print("A tömbben {} db '9-es' van.".format(auxvar))
