#Operasi komparasi

#-hasilnya boolean 

a = 4
b = 2

#-lebih besar dari (>)
print("====Lebih besar dari (>)====")
hasil = a > 3
print(a, ">", 3, "=", hasil)

hasil = b > 3 
print(b, ">", 3, "=", hasil)

hasil = b > 2 #jika nilai sama, hasil akan false
print(b, ">", 2, "=", hasil)

#-lebih kecil dari (<)
print("====Lebih kecil dari (<)====")
hasil = a < 3
print(a, "<", 3, "=", hasil)

hasil = b < 3 
print(b, "<", 3, "=", hasil)

hasil = b < 2
print(b, "<", 2, "=", hasil)

#-lebih dari sama dengan (>=)
print("====Lebih dari sama dengan (>=)====")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)

hasil = b >= 3 
print(b, ">=", 3, "=", hasil)

hasil = b >= 2 #jika nilai sama, hasil akan true
print(b, ">=", 2, "=", hasil)

#-kurang dari sama dengan (<=)
print("====Kurang dari sama dengan (<=)====")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)

hasil = b <= 3 
print(b, "<=", 3, "=", hasil)

hasil = b <= 2 #jika nilai sama, hasil akan true
print(b, "<=", 2, "=", hasil)

#-sama dengan (==)
print("====Sama dengan (==)====")
hasil = a == 4
print(a, "==", 4, "=", hasil)

hasil = b == 4 
print(b, "==", 4, "=", hasil)

#-tidak sama dengan (!=)
print("====Tidak sama dengan (!=)====")
hasil = a != 4
print(a, "!=", 4, "=", hasil)

hasil = b != 4 
print(b, "!=", 4, "=", hasil)

#-is sebagai komparasi objek identity (is)
print("====Object identity (is)====")
x = 5
y = 5
print("Nilai x=", x, "id=", hex(id(x))) #jika nilai sama, akan disimpan ke memori yg sama juga, maka id sama
print("Nilai y=", y, "id=", hex(id(y)))
hasil = x is y
print("x is y=", hasil)

x = 5
y = 6
print("\nNilai x=", x, "id=", hex(id(x))) 
print("Nilai y=", y, "id=", hex(id(y)))
hasil = x is y
print("x is y=", hasil)

#-is not sebagai komparasi objek identity (is not)
print("====Object identity (is not)====")
x = 5
y = 5
print("Nilai x=", x, "id=", hex(id(x))) #jika nilai sama, akan disimpan ke memori yg sama juga, maka id sama
print("Nilai y=", y, "id=", hex(id(y)))
hasil = x is not y
print("x is not y=", hasil)

x = 5
y = 6
print("\nNilai x=", x, "id=", hex(id(x))) 
print("Nilai y=", y, "id=", hex(id(y)))
hasil = x is not y
print("x is not y=", hasil) 
