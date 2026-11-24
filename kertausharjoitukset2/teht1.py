def laske_kustannus(valmistuskustannus, maara):
    kokonaiskustannus = valmistuskustannus * maara
    return kokonaiskustannus

#paaohjelma

valmistuskustannus = float(input("Anna tuotteen valmistuskustannus (€): "))
maara = int(input("Kuinka monta tuotetta valmistetaan? "))

tulos = laske_kustannus(valmistuskustannus, maara)


print("Valmistuksen kokonaiskustannus: ", tulos, "€")