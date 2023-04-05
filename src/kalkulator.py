#Percabangan

#kalkulator sederhan
print("==============Kalkulator==============")
angka_1 = float(input("Angka 1: "))
operator = input("Operator (+,-,*,/: ")
angka_2 = float(input("Angka 2: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya= {hasil}")

elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya= {hasil}")

elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya= {hasil}")

elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya= {hasil}")
else:
    print("Operator tidak ditemukan") 
