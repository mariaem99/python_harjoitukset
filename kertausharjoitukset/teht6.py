arvot = []

while True:
    arvo = int(input("Syötä arvoja (0 lopettaa): "))

    if arvo == 0:
     break

    arvot.append(arvo)

print("Arvot pienimmästä suurimpaan: ", sorted(arvot))
print("Arvot listausjärjestyksessä: ", arvot)