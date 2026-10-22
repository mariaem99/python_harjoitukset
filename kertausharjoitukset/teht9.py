tuotteet = []
maarat = []

while True:

    tuote = input("Mita tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaanko = input("Jatketaako tuotantoa? ")

    if jatketaanko == "Ei" or jatketaanko == "ei":
        break


print("Tuotanto lopetettu!")
print("Valmistetut tuotteet: ")

for i in range(len(tuotteet)):
        print(tuotteet[i] + ":", maarat[i], "kpl")