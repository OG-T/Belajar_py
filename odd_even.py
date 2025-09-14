print(16 % 3) # hasilnya 1 (sisa bagi 1)

print(22 % 3) # hasilnya 1 (sisa bagi 1)

print(65 % 3) # hasilnya 2 (sisa bagi 2)


input_user = int(input("Masukkan angka: "))

if input_user % 2 == 0:
    print(f"{input_user} adalah bilangan genap.")
else:
    print(f"{input_user} adalah bilangan ganjil.")