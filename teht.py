ostoslista = ["maito", "leipa", "juusto", "omena"]

while len(ostoslista) > 0:
    tuote = input("Syötä tuote: ")

    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("Tuote poistettu listasta")
        print("Jäljellä olevat tuotteet:", ostoslista)
    else:
        print("Tuotetta ei ole ostoslistassa.")

print("Homma on hoidossa!")