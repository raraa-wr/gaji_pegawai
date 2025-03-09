# menentukan total gaji
nama = str(input("nama anda: "))
nik = int(input("nik anda: "))
status = str(input("status anda: "))
if status == "pegawai tetap" :
    gaji_pokok = 1000000
    golongan = str(input("golongan anda (A/B/C): "))
    if golongan == "A" :
        bonus = 200000
    elif golongan == "B" :
        bonus = 400000  
    elif golongan == "C" :
        bonus = 600000
    else : raise ValueError("golongan tidak valid")
    gaji_total = gaji_pokok + bonus
    print("<<< rincian gaji >>>")
    print(f"Nama :", nama)
    print(f"NIK :", nik)
    print(f"status :", status)
    print(f"golongan :", golongan)
    print("gaji pokok: ", gaji_pokok)
    print("bonus: ", bonus)
    print("gaji total: ", gaji_total)
elif status == "honor" :
    gaji_pokok_honor= 750000
    golongan = str(input("golongan anda: "))
    if golongan == "A" :
        bonus = 150000
        gaji_pokok_honor += bonus
    elif golongan == "B" :
        bonus = 275000
        gaji_pokok_honor += bonus
    elif golongan == "C" :
        bonus = 480000
    else : raise ValueError("golongan tidak valid")
    gaji_total_honor = gaji_pokok_honor + bonus
    print("<<< rincian gaji >>>")
    print(f"Nama :", nama)
    print(f"NIK :", nik)
    print(f"status :", status)
    print(f"golongan :", golongan)
    print("gaji pokok: ", gaji_pokok_honor)
    print("bonus: ", bonus)
    print("gaji total: ", gaji_total_honor)
else :
    print("status tidak valid")