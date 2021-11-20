import random

#tömb feltöltve véletlen számokkal

veletlenSzamok = []

for i in range(10):
    veletlenSzamok.append(random.randint(0, 100))

#a tömb elemeinek kiíratása
for szam in veletlenSzamok:
    print(szam)

#számok átlaga

atlag = 0

for szamok in veletlenSzamok:
    atlag += szamok

print("A tömb elemeinek átlaga: {0}".format(atlag / len(veletlenSzamok)))

#a tömb legkisebb eleme

legkisebb = veletlenSzamok[0]

for szam in veletlenSzamok:
    if legkisebb > szam:
        legkisebb = szam

print("A tömb legkisebb eleme: {0}".format(legkisebb))

#a tömb legnagyobb eleme

legnagyobb = veletlenSzamok[0]

for szam in veletlenSzamok:
    if legnagyobb < szam:
        legnagyobb = szam

print("A tömb legnagyobb eleme: {0}".format(legnagyobb))

#van benne páros szám?

van = False

for szam in veletlenSzamok:
    if szam % 2 == 0:
        van = True

if van == True:
    print("A tömb tartalmaz páros számot!")
else: 
    print("A tömb nem tartalmaz páros számot!")

#az ötvennél nagyobbak összege

tmp = 0

for szam in veletlenSzamok:
    if szam > 50:
        tmp += szam

print("Az 50-nél nagyobb számok összege: {0}".format(tmp))

#hány 9-es van benne?

tmp = 0

for szam in veletlenSzamok:
    if szam == 9:
        tmp += 1

print("A tömbben {} db '9' van.".format(tmp))
