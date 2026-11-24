hedelmat = {
    "kiivi" : 2.4,
    "omena" : 1.8,
    "banaani" : 1.4
}

yhteensa = 0

while True:

    hedelma = input("Anna hedelmät (syötä tyhjä lopettaaksesi): ")

    if hedelma == "":
           break

    if hedelma in hedelmat:
     print("Hedelmän", hedelma, "hinta:", hedelmat[hedelma], "€/kg")
     yhteensa = yhteensa + hedelmat [hedelma]

    else:
       lisaa = input("Hedelmää ei löydy, lisätäksesi hedelmän, paina 1: ")
       if lisaa == "1":
           hinta = float(input("Anna hedelman hinta (€): "))
           hedelmat[hedelma] = hinta
           yhteensa = yhteensa + hinta


print("Yhteensä hinta: ", yhteensa, "€")
print("Päivitetty hinnasto: ", hedelmat)