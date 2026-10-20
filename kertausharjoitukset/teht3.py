while True:
    print("Tuote valmistettu!")
    jatketaanko = input("Jatketaanko tuotantoa? ")

    if jatketaanko == "ei" or jatketaanko == "Ei" or jatketaanko == "EI":
        break
print("Tuotanto lopetettu!")