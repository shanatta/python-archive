#Perulangan For Loop

#-for kondisi:
#-    aksi

#-dengan list
angka2 = [0,2,4,8,10] #list
print("=============Dengan List=============")
print(angka2)

for i in angka2:
    print(f"i sekarang= {i}")

print("end 1")

#-dengan range
angka2_range = range(5)
print("=============Dengan Range=============")
for i in angka2_range:
    print(f"i sekarang= {i}")

print("end 2")

angka2_range = range(1,10) #dimulai dari 1
print("-------------------------------------")
for i in angka2_range:
    print(f"i sekarang= {i}")

print("end 3")

angka2_range = range(1,10) #dimulai dari 1
print("-------------------------------------")
for i in angka2_range:
    print("azeril baik")

print("end 3")

#-dengan string
print("============Dengan String============")
data_str = "azeril baihaqy"
for huruf in data_str:
    print(huruf)

print("end 4") 
