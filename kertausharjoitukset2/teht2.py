def laske_voitto(valmistuskustannus, myyntihinta, maara):
    kokonaistulos = (myyntihinta - valmistuskustannus) * maara

    return kokonaistulos

#paaohjelma

valmistuskustannus = float(input("Anna tuotteen valmistuskustannus (€): "))
myyntihinta = float(input("Anna tuotteen myyntihinta (€): "))
maara = int(input("Kuinka monta tuotetta myytiin? "))

voitto = laske_voitto(valmistuskustannus, myyntihinta, maara)

print("Kokonaisvoitto: ", voitto, "€")

if voitto < 0:
    print("Tuotanto on tappiollista!")

else:
    print("Tuotanto on kannattavaa!")