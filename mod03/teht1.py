pituus = float(input("Anna kuhan pituus senttimetreinä: "))
if pituus >= 37:
    print("Kuha on normaalimittainen. ")
else:
    print("Laske kuha järveen. ")
    print("Alimmasta sallitusta pyyntimitasta puuttuu", 37 - pituus, "cm. ")