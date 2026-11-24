varasto = {
    "pöytä": 20,
    "tuoli": 50,
    "hylly": 15
}

print("Varastotilanne: ")

for tuote in varasto:
    print(tuote, ":", varasto[tuote], "kpl")


tuote = input("Mitä tuotetta lisätään varastoon: ")
tuote = tuote.lower()
maara = int(input("Kuinka monta lisätään: "))

if tuote in varasto:
    varasto[tuote] = varasto[tuote] + maara
else:
    varasto[tuote] = maara

print("Päivitetty varastotilanne: ")

for tuote in varasto:
    print(tuote, ":", varasto[tuote], "kpl")

