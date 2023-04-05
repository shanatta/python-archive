#Operator Assignment

#operasi yg dapat dilakukan dengan penyingkatan

a = 5 #assignment
print("Nilai a= ", a)

#-tambah
a += 1 #artinya a= a+1
print("Nilai a+= 1, nilai a= ", a)

#-akurang
a -= 2 #artinya a= a-2
print("Nilai a-= 2, nilai a= ", a)

#-kali
a *= 5 #artinya a= a*5
print("Nilai a*= 5, nilai a= ", a)

#-bagi
a /= 2 #artinya a= a/2
print("Nilai a/= 2, nilai a= ", a)

b = 10 #assignment 2
print("\nNilai b= ", b)

#-floor division
b //= 3 #artinya b= b//3
print("Nilai b//= 3, nilai b= ", b)


b = 10 #assignment 3
print("\nNilai b= ", b)

#-modulus
b %= 3 #artinya b= b%3
print("Nilai b%= 3, nilai b= ", b)

a = 5 #assignment 4
print("\nNilai a= ", a)

#-pangkat
a **= 3 #artinya a= a**3
print("Nilai a**= 3, nilai a= ", a)

#-operasi bitwise OR
c = True
print("==========Operasi Bitwise OR==========")
print("Nilai c= ", c)
c |= False
print("Nilai c|= False, nilai c menjadi", c) #true false= true

c = False
print("Nilai c= ", c)
c |= False
print("Nilai c|= False, nilai c menjadi", c) #false false= false

#-operasi bitwise AND
c = True
print("=========Operasi Bitwise AND=========")
print("Nilai c= ", c)
c &= False
print("Nilai c&= False, nilai c menjadi", c) #true false= false

c = True
print("Nilai c= ", c)
c &= True
print("Nilai c&= True, nilai c menjadi", c) #true true= true

#-operasi bitwise XOR
c = True
print("=========Operasi Bitwise XOR=========")
print("Nilai c= ", c)
c ^= False
print("Nilai c^= False, nilai c menjadi", c) #true false= true

c = True
print("Nilai c= ", c)
c ^= True
print("Nilai c^= True, nilai c menjadi", c) #true true= false

#-shifting 
print("==============Shifting==============")
d = 0b0100
print("Nilai d= ", format(d, '04b'))
d >>= 2
print("Nilai d>>= 2, nilai d menjadi", format(d, '04b'))
d <<= 1
print("Nilai d<<= 1, nilai d menjadi", format(d, '04b')) 
