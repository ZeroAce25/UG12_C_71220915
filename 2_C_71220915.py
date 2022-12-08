lini = input("Masukkan angka: ")
bil = input("Masukkan angka yang dihitung: ")
plus = 0
for i in range(len(lini)):
    if lini[i] == bil:
        plus += 1

print("bil{} muncul sebanyak {} kali".format(bil,plus))
