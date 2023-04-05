#Date and Time

import datetime as dt

hari_ini = dt.date.today()
print("============Date and Time============")
print(hari_ini)
print(f"Hari ini adalah hari= {hari_ini:%A}")

tanggal = dt.date(2023,4,4)
print("-------------------------------------")
print(tanggal)
print(f"Hari ini adalah hari= {tanggal:%A}")

print("==============Exercise==============")
print("Masukan tanggal lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"\nTanggal lahir anda= {tanggal_lahir}")
print(f"Hari= {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal= {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days // 365) //30
print(f"Umur anda=  {umur_tahun} tahun {umur_bulan} bulan") 
