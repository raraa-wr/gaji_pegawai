gaji_pokok_list = {
    "pegawai tetap": 1000000,
    "honor": 750000
}

bonus_list = {
    "A": {"pegawai tetap": 200000, "honor": 150000},
    "B": {"pegawai tetap": 400000, "honor": 275000},
    "C": {"pegawai tetap": 600000, "honor": 480000}
}

for status in gaji_pokok_list:
    for golongan in bonus_list:
        gaji_pokok = gaji_pokok_list[status]
        bonus = bonus_list[golongan][status]
        gaji_total = gaji_pokok + bonus
        

        print("\n Rincian Gaji")
        print(f"Status: {status}")
        print(f"Golongan: {golongan}")
        print(f"Gaji Pokok: Rp{gaji_pokok:,}")
        print(f"Bonus: Rp{bonus:,}")
        print(f"Gaji Total: Rp{gaji_total:,}")
