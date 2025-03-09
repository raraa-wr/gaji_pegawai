# menghitung umur
umur = int(input("Umur anda: "))
if umur <= 5 :
    print("belita")
elif 13>= umur > 15 :
    print("anak-anak")
elif 25>= umur > 13 :
    print("remaja")
elif 35>= umur > 25 :
    print("dewasa")
elif 55>= umur > 35 :
    print("orang tua")
elif 99>= umur > 55 :
    print("lansia")
else :
    print("umur tidak valid")
