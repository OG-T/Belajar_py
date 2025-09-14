# operator
# operator adalah simbol atau karakter khusus yang digunakan untuk melakukan operasi pada variabel dan nilai 
# pyhton memiliki beberapa jenis operator 

# 1. operator aritmatika (matematika)
# operator aritmatika digunakan untuk melakukan operasi matematika pada angka
# + -> penjumlahan
# - -> pengurangan
# * -> perkalian
# / -> pembagian
# // -> pembagian bulat (hasilnya dibulatkan ke bawah)
# % -> modulus (sisa bagi)
# ** -> pangkat

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)
print(a % b)

a = 2
b = 3

print(a ** b)

x = 10 
print("x awal :", x)

x += 5 # sama dengan: x = x + 5
print("x setelah ditambah 5 :", x) # 15

x -= 3 # sama dengan: x = x - 3
print("x setelah dikurang 3 :", x) # 12

x *= 2 # sama dengan: x = x * 2
print("x setelah dikali 2 :", x) # 24

x /= 4 # sama dengan: x = x / 4
print("x setelah dibagi 4 :", x) # 6.0

x //= 2 # sama dengan: x = x // 2
print("x setelah dibagi bulat 2 :", x) # 3.0 

x %= 2 # sama dengan : x = x % 2
print("x setelah di modulus 2 :", x) # 1.0

x **= 3 # sama dengan : x = x ** 3
print("x setelah dipangkat 3 :", x) # 1.0 

# operator perbandingan
# operator perbandingan digunakan untuk membandingkan dua nilai
# hasil dari operator perbandingan adalah boolean (True/False)

print(a > b) #
print(a < b) 
print(a >= b) 
print(a <= b) 
print(a == b)
print(a != b) 
