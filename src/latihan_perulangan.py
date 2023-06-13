#Latihan Perulangan Membuat Segitiga

sisi = 10

#-menggunakan for
#-dummy variable
print("============For Loop============")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

#-menggunakan while
print("===========While Loop===========")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

#-hanya ganjil saja
print("========While Loop Ganjil========")
count = 1
spasi = int (sisi/2)
print(spasi)
while True:
    if (count %2):
        #-print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        #-kembali keatas jika ganjil
        spasi -= 1
        count += 1
        continue

    #-break jika count melebihi sisi
    if count > sisi:
        break 
