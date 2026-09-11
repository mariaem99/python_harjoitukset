hyttiluokka = input("Anna hyttiluokka (A, B, C, LUX): ")

if hyttiluokka == "A" or hyttiluokka == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella. ")
elif hyttiluokka == "B" or hyttiluokka == "b":
    print("B on ikkunaton hytti autokannen yläpuolella. ")
elif hyttiluokka == "C" or hyttiluokka == "c":
    print("C on ikkunaton hytti autokannen alapuolella. ")
elif hyttiluokka == "LUX" or hyttiluokka == "lux":
    print("LUX on parvekkeellinen hytti yläkannella. ")
else:
    print("Virheellinen hyttiluokka. ")