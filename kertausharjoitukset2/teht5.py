oppilaat = {
    "Maria" : ["Matematiikka", "Ohjelmointi", "Rahoitus"],
    "Aino" : ["Matematiikka", "Taloustiede"],
    "Jaakko" : ["Taloustiede", "Markkinointi", "Johtaminen"]
}

for oppilas in oppilaat:
     print(oppilas, ":", oppilaat[oppilas])

uusi = input("Anna uuden oppilaan nimi: ")

kurssit = []

while True:
     kurssi = input("Anna kurssi yksi kerrallaan(lopeta ohjelma syöttämällä tyhjä merkki): ")

     if kurssi == "":
      break

     kurssit.append(kurssi)

oppilaat[uusi] = kurssit

for oppilas in oppilaat:
    print(oppilas, oppilaat[oppilas])

def laske_osallistujat(oppilaat):
    kurssi = input("Syötä kurssi, jonka osallistujamäärän haluat tarkistaa: ")
    maara = 0

    for oppilas in oppilaat:
        if kurssi in oppilaat[oppilas]:
            maara = maara + 1

    print("Kurssin osallistujamäärä: ", maara)

while True:

    laske_osallistujat(oppilaat)
    jatko = input("Haluatko tarkistaa toisen kurssin tiedot? Syötä 1 jatkaaksesi, Syötä 2 lopettaaksesi: ")
    if jatko == "2":
        break