nama = input("masukan nama anda: ")
print("Hello", nama)

umur_anda = input("masukan umur anda: ")
print("umur anda adalah", umur_anda)
print("tipe umur", type(umur_anda))

# konversi tipe data (mengubah data dari satu tipe ke tipe lain
# beberapa fungsi konversi di python
# int() -> mengubah ke tipe data integer (bilangan bulat)
# float() -> mengubah ke tipe data float (bilangan desimal)
# str() -> mengubah ke tipe data string (teks)
# bool() -> mengubah ke tipe data boolean (True/False)  

nama = input("Masukan nama anda: ")
print("Hello", nama)

umur_teks = input("Masukan umur anda: ")
umur = int(umur_teks)
print("umur anda adalah", umur)
print("tipe umur", type(umur))

tinggi_teks = input("Masukan tinggi badan anda (dalam cm): ")
tinggi = float(tinggi_teks)
print("tinggi badan anda adalah:",tinggi)
print("tipe tinggi badan:", type(tinggi))

