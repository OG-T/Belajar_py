#string dan manipulasi string

# apa itu string? 
# ring adalah tipe data untuk menyimpan teks atau kumpulan karakter 
# string ditulis dengan menggunakan tanda kutip, baik tunggal (' ') atau ganda (" ")

#menggabungkan string 
# untuk menggabungkan string kita bisa menggunakan tanda + (tambah)
# dan tipe data string tidak bisa digabungkan dengan tipe data lain, kita harus konversikan dahulu tipe data lain ke tipe data string 

nama = "Arif"
umur = 21

# cara yang salah (akan error)
# print("nama saya " + nama + ", umur ", umur)

# cara yang benar 
pesan = "nama saya: " + nama + ", umur: " + str(umur)
print(pesan)

# panjang string
# untuk mengetahui panjang string kita bisa menggunakan fungsi len()

print(len(nama))  
print(len(pesan))  

# mengakses karakter dalam string
# untuk mengakses karakter dalam string kita bisa menggunakan indexing
# indexing dimulai dari 0 untuk karakter pertama, 1 untuk karakter kedua, dan seterusnya 
# untuk mengakses tiap karakter kita bisa menggunakan kurung kotak [] dan di dalam kurung kotak tersebut disebutkan posisi index nya
# kita juga bisa menggunakan index negatif jika kita ingin mengakses karakter dari belakang

nama = "pyhton"
print(nama[0])   # p
print(nama[1])   # y
print(nama[2])   # t

nama = "python"
print(nama[-1])  # n
print(nama[-2])  # o
print(nama[-3])  # h

#string slicing
# slicing adalah mengambil sebagian karakter dari string
# untuk melakukan slicing kita bisa menggunakan tanda [awal:akhir]

nama = "python"
print(nama[0:3])  # pyt (karakter ke 0,1,2)
print(nama[2:])   # thon (karakter ke 2 sampai akhir)

#jika tidak menyebutkan nilai awal, makan akan diambil dari awal string
print(nama[:3])   # pyt (karakter ke 0,1,2)
#jika tidak menyebutkan nilai akhir, maka akan diambil sampai akhir string
print(nama[2:])   # thon (karakter ke 2 sampai akhir)
#jika tidak menyebutkan nilai awal dan akhir, maka akan diambil seluruh karakter
print(nama[:])    # python (seluruh karakter)       

#string method
# method adalah fungsi yang dimiliki oleh sebuah tipe data (ada banyak sekali method di python)
# contoh method pada string
# upper() -> mengubah semua karakter menjadi huruf besar
# lower() -> mengubah semua karakter menjadi huruf kecil
# capitalize() -> mengubah karakter pertama menjadi huruf besar  
# title() -> mengubah karakter pertama dari setiap kata menjadi huruf besar
# strip() -> menghapus spasi di awal dan akhir string     
# replace() -> mengganti karakter tertentu dengan karakter lain
# find() -> mencari posisi karakter tertentu dalam string

nama = "jazariarif"
print(nama)
nama_upper = nama.upper()
print(nama_upper) # JAZARIARIF

print(nama)
nama_lower = nama.lower()
print(nama_lower) # jazariarif

nama = "muhammad jazari"
print(nama)
nama_title = nama.title()
print(nama_title) # hasilnya : Muhammad Jazari

print(nama)
nama_capitalize = nama.capitalize()
print(nama_capitalize) # hasilnya : Muhammad jazari

nama = "   arif   "
print(nama)
nama_strip =  nama.strip()
print(nama_strip) #hasilnya : arif

nama = "i love java"
print(nama)
nama_replace = nama.replace("java", "python")
print(nama_replace) # hasilnya : i love python

nama = "muhammad jazari arif bayhakin"
jumlah_m = nama.count("m")
print(jumlah_m) # hasilnya : 2

kalimat = "belajar python"
posisi = kalimat.find("python")
print(posisi) # hasilnya : 8

# escape karakter 
# escape karakter merupakan karakter karakter khusus dalam string yang diawali dengan tanda backslash (\)
# contoh escape karakter
# \n -> newline (baris baru)
# \t -> tab (spasi 4 karakter)
# \\ -> backslash (tanda backslash itu sendiri)
# \"dan\' (kutip dalam string), perlu menambahkan (\)

kalimat = "Baris pertama\nBaris Kedua"
print(kalimat)

kalimat = "Nama:\tArif\nUmur:\t21"
print(kalimat)

lokasi = "C:\\\\User\\Arif\\Documents"
print(lokasi)

kalimat = "Dia berkata: \"Halo, apa kabar?\""
print(kalimat)


# string interpolation (f-string)
# f-string adalah cara untuk menyisipkan variabel ke dalam string dengan cara yang lebih mudah dan efisien tanpa harus menggunakan tanda + (tambah)
 
# contoh menerapakn f-string 

nama = "arif"
umur = 21
tinggal = "jakarta"

kalimat = f"nama: {nama}, umur: {umur} tahun, tinggal di: {tinggal}"
print(kalimat)

# lebih jelas dibandingkan dengan cara biasa (koversi)

kalimat = "nama: " + nama +",umur : " + str(umur) + " tahun, tinggal di: " + tinggal
print(kalimat)

# dan f-string juga dapat mengeksekusi ekspresi di dalamnya

harga = 10000
jumlah = 5

#operasi dalam f-string 
total_harga = f"total harga: Rp.{harga * jumlah}"
print(total_harga)

# method calls dalam f-string
nama = "arif"
salam = f"Hello {nama.upper()}"
print(salam)


