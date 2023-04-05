#Operasi aritmatika

a = 10
b = 3

#-operasi tambah
hasil = a+b
print(a, "+", b, "=", hasil)

#-operasi kurang
hasil = a-b
print(a, "-", b, "=", hasil)

#-operasi kali
hasil = a*b
print(a, "x", b, "=", hasil)

#-operasi bagi
hasil = a/b
print(a, ":", b, "=", hasil) #otomatis jadi float

#-operasi eksponen (pangkat)
hasil = a**b
print(a, "**", b, "=", hasil) 

#-operasi modulus (sisa bagi)
hasil = a%b
print(a, "%", b, "=", hasil) 

#-operasi floor division
hasil = a//b
print(a, "//", b, "=", hasil) 

#-prioritas operasi
#-()
#-eksponen
#-perkalian, pembagian, modulus, floor division
#-pertambahan & pengurangan

a=3
b=2
c=4

hasil = a ** b * c + a / b - b % c // a
print("Contoh 1=", hasil)

hasil = a + b * c
print("Contoh 2=", hasil)

hasil = (a + b) * c #tanda kurung diselesaikan dulu
print("Contoh 3=", hasil) 
