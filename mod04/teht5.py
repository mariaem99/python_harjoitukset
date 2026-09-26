yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "suklaabanaani" and salasana == "koira":
        print("Tervetuloa")
        break

    print("Väärä käyttäjätunnus tai salasana")
    yritykset = yritykset + 1

    if yritykset == 5:
        print("Pääsy evätty")