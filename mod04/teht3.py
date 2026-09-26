print("Syota tyhja merkki lopettaaksesi")
luku = input("Anna luku: ")

pienin = 10
suurin = 1

while True:
    luku = int(input("Anna luku (1-10): "))

    if luku < pienin:
        pienin = luku

    if luku > suurin:
        suurin = luku

    print("Pienin:", pienin)
    print("Suurin:", suurin)

    if luku == " ":
        break