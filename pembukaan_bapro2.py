X = int(input("X="))
Y = int(input("Y="))

Z = X + Y
print(type(Z))
print("hasil dari Z", Z)

a = int(input("a="))
if a % 2 == 0: 
    print(a,"adalah bilangan genap")
else:
    print(a,"adalah bilangan ganjil")
## menghitung luas segitiga

alas = float(input("Alas="))
tinggi = float(input("Tinggi="))
luas_segitiga = 0.5 * alas * tinggi
print("Luas segitiga", luas_segitiga)

## menghitung luas persegi panjang
panjang = float(input("Panjang="))
lebar = float(input("Lebar="))
luas_persegi_panjang = panjang * lebar

print("Luas persegi panjang", luas_persegi_panjang)

## menghitung luas lingkaran
import math

r = float(input("Jari-jari="))
luas_lingkaran = math.pi * (r ** 2)
print("Luas lingkaran", luas_lingkaran)

## menghitung luas tabung

r = float(input("Jari-jari="))
t = float(input("Tinggi="))
luas_tabung = 2 * math.pi * r * (r + t)
print("Luas tabung", luas_tabung)

## hitung volume tabung

r = float(input("Jari-jari="))
t = float(input("Tinggi="))
volume_tabung = math.pi * (r ** 2) * t
print("Volume tabung", volume_tabung)





    
    


