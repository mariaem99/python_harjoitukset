hedelmien_hinnat = {
    "Omena": 0.54,
    "Banaani": 0.67,
    "Päärynä": 0.73,
    "Mandariini": 0.39,
}

hedelma = input("Anna hedelmän nimi: ")

if hedelma in hedelmien_hinnat:
    print("Hedelmän",hedelma, "hinta on", hedelmien_hinnat[hedelma], "€/kpl")
else:
    print("Hedelmää ei löytynyt.")
