leiviskat = float(input("Anna leiviskat: "))
naulat = float(input("Anna neulat: "))
luodit = float(input("Anna luodit: "))

luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luodit_yhteensa * 13.3

kilot = int(grammat // 1000)
grammat_jaljella = grammat % 1000

print("Massa nykymittojen mukaan:", kilot, "kilogrammaa ja", grammat_jaljella, "grammaa.")