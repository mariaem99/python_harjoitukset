tuntipalkka = float(input("Syota tuntipalkka: "))
tunnit = float(input("Syota tehdyt tunnit: "))
viikonpaiva = input("Anna viikonpaiva: ")

if viikonpaiva == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print("Päiväpalkka on", paivapalkka, "euroa")