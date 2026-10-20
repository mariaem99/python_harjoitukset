from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku saadaksesi neliöjuuren tai syötä nolla lopettaaksesi: "))

    if luku < 0:
        print("Virheellinen numero")

    elif luku > 0:
        print(sqrt(luku))

    elif luku == 0:
        break

print("Ohjelma lopetettu")