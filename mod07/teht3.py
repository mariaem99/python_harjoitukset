lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto. Uusi lentoasema, valitse 1.  Lentoaseman haku, valitse 2. Ohjelman lopetus, valitse 3.: ")

    if toiminto == "1":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat [koodi] = nimi

    if toiminto == "2":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        for koodi in lentoasemat:
         print(nimi)
        else:
           print("Lentoasemaa ei löydy listasta.")

    if toiminto == "3":
     print("Ohjelma on päättynyt. Kiitos!")
     break