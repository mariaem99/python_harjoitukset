import random

salainen_luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku: "))

    if arvaus < salainen_luku:
        print("Liian pieni arvaus")

    if arvaus > salainen_luku:
        print("Liian suuri arvaus")

    if arvaus == salainen_luku:
        print("Oikein")
        break