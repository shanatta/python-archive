#Continue dan Pass

#-pass berfungsi sebagai dummy (tidak dieksekusi)
angka = 0

print("=================Pass=================")
while angka < 5:
    angka += 1

    if angka == 3:
        pass 
   
    print(angka)

#-continue
angka = 0
print("===============Continue===============")

print(f"angka sekarang= {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang= {angka}")

    if angka == 3:
        print("nice")
        continue #loop meloncat ke step selanjutnya

    print("hai") #aksi 2

print("end") 
