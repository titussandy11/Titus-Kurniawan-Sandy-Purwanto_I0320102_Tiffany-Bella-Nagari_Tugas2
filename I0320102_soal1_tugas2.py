#Titus Kurniawan Sandy Purwanto
#I0320102
#Kelas C
#Soal Latihan Nomor 1
print("Aplikasi Hitung Luas Persegi Panjang")
panjang = float(input("panjang: "))
lebar   = float(input("lebar: "))
luas = panjang*lebar
print("Luas persegi panjang = ", luas)

print("Aplikasi Hitung Luas Lingkaran")
r = float(input("Jari-jari: "))
luas_lingkaran = 3.14*(r**2)
print("Luas lingkaran =", luas_lingkaran)

print("Aplikasi Hitung Luas Permukaan Kubus")
rusuk = float(input("panjang rusuk kubus: "))
luas_permukaan_kubus = (6*rusuk*rusuk)
print("Luas permukaan kubus: ", luas_permukaan_kubus)

print("Program konversi suhu celcius ke farenheit")
celcius = float(input("masukan skala celcius: "))
konversi_farenheit = 9 * celcius / 5 +32
print(f"Hasil konversi suhu {celcius} adalah {konversi_farenheit} Farenheit")

print("Program konversi suhu reamur ke kelvin")
reamur = float(input("masukan skala reamur: "))
konversi_kelvin = 5 * reamur / 4 +273
print(f"Hasil konversi suhu {reamur} adalah {konversi_kelvin} Kelvin")



