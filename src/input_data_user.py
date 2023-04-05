#Input data user

#-input string
nama = input("Masukan nama: ")
print("Welcome", nama, type(nama)) #semua jadi string

#-input float
angka = float(input("Masukan angka: "))
print("Data=", angka, "type=", type(angka)) 

#-input boolean
bool = bool(int(input("Masukan nilai boolean: ")))
print("Data=", bool, "type=", type(bool)) #dari boolean di konvers int, baru ke boolean lagi 
