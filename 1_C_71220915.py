def reverse(ab):
    str = ""
    for i in ab:
        str = i + str
    return str

ab = str(input("Masukan Kata atau angka : "))
print(reverse(ab))
