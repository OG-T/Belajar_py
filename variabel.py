# Variabel
# Membuat Variabel seperti memberi label pada sebuah kotak
nama = "arif"     #   variabel bernama 'nama' berisi text "arif"
umur = 21       #   variabel bernama 'umur' berisi angka 21
tinggi = 170.5  #   variabel bernama 'tinggi' berisi angka desimal 170.5
# variabel digunakan untuk kita menyimpan data 
# aturan penamaan variabel

namaanda = "arif"  # boleh
nama_anda = "arif" # boleh
NamaAnda = "arif"  # boleh

# Tipe Data
# ada 4 tipe data dasar di python
# 1. String (str) -> teks / kalimat
# 2. Integer (int) -> bilangan bulat
# 3. Float (float) -> bilangan desimal
# 4. Boolean (bool) -> True / False

# tipe data string (str)
# string dengan singel quote
nama = 'arif'
kota = 'jakarta'
alamat = 'jl. merdeka no 10'

# string dengan double quote
nama2 = "arif"
kota2 = "jakarta"
alamat2 = "jl. merdeka no 10"

#string dengan triple quote (bisa untuk multiline)
puisi = """
ini adalah puisi
yang terdiri 
dari beberapa kata dan baris
"""

# string kosong 
empty_string = ""
another_empty_string = ''   

print(type(puisi))                 # <class 'str'>

# tipe data integer (int)
# bilangan bulat positif dan negatif 
umur = 21
tahun_lahir = 2004
saldo = -100000
nol = 0

# bilangan besar (python bisa handel bilangan yang sangat besar)

populasi_dunia = 10000000000
angka_besar = 1234567890123456789

print(type(umur))           # <class 'int'>
print(type(angka_besar))    # <class 'int'>


# tipe data float (bilangan desimal)
tinggi = 170.5
berat = 66.2
pi = 3.14
suhu = -10.5

# notasi sintifik
speed_of_light = 3e8    # 3 x 10^8 = 300000000
very_small = 1e-6       # 1 x 10^-6 = 0.000001

print(type(tinggi))            # <class 'float'>
print(type(speed_of_light))    # <class 'float'>

# tipe data boolean (bool)
is_student = True       # perhartikan T dan F nya harus kapital (karna python case sensitive )
is_graduated = False
has_license = True

print(type(is_student))    # <class 'bool'>


# assigment dasar
nama = "arif"
umur = 21
tinggi = 170.5
is_student = True

# multi assigment
x = y = z = 0
a, b, c = 1, 2, 3       # a=1, b=2, c=3
name, age = "arif", 21  # name = "arif", age = 21

# mengubah nilai variabel
skor = 10
print(skor) # 10
skor = 15   # mengubah nilai variabel skor menjadi 15
print(skor) # 15 

# menggunakan variabel dalam operasi
nama_depan = "arif"
nama_belakang = "setiawan"
nama_lengkap = nama_depan + " " + nama_belakang  # menggabung string

panjang = 10
lebar = 5
luas = panjang * lebar  # operasi perkalian

# menggunakan variabel dalam print 
print("nama lengkap : ", nama_lengkap)
print("luas persegi panjang : ", luas) 

