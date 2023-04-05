#Operasi logika/boolean

#-not, or, and, xor

#-not (kebalikan)
print("====Not====")
a = True
c = not a
print("Data a=", a)
print("Data c=", c)

a = False
c = not a
print("\nData a=", a)
print("Data c=", c)

#-or (salah satu true, hasilnya true)
#-seperti operasi penjumlahan 0+1
print("====Or====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = False
b = True
c = a or b
print(a, "OR", b, " =", c)

a = True
b = False
c = a or b
print(a, " OR", b, "=", c)

a = True
b = True
c = a or b
print(a, " OR", b, " =", c)

#-and (salah satu false, hasilnya false)
#-akan bernilai true jika keduanya true
#-seperti operasi perkalian 
print("====And====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = False
b = True
c = a and b
print(a, "AND", b, " =", c)

a = True
b = False
c = a and b
print(a, " AND", b, "=", c)

a = True
b = True
c = a and b
print(a, " AND", b, " =", c)

#-xor (akan true jika salah satu true)
#true dengan true jadi false
print("====Xor====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)

a = True
b = False
c = a ^ b
print(a, " XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, " XOR", b, " =", c) 
