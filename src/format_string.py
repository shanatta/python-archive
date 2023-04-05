#Format String

#-string
nama = "Kanaya"
format_str = f"Hello {nama}"
print("=============String=============")
print(format_str)

#-angka 
angka = 2005.5
format_str = f"Angka= {angka}"
print("==============Angka==============")
print(format_str)

#-bilangan bulat
angka = 28 #ga pake koma/int
format_str = f"Bilangan bulat= {angka}" #pake :d biar true= bulat
print("----------------------------------") 
print(format_str)

#-bilangan ordo ribuan
angka = 3000000
format_str = f"Bilangan jutaan= {angka:,}" #pake (,) hasilnya 3,000,000 kalo ga pake jadi 3000000
print("----------------------------------") 
print(format_str)

#-bilangan desimal 
angka = 2005.2912
format_str = f"Angka= {angka:.2f}" # (.2f) ambil 2 angka belakang koma, f= float
print("----------------------------------") 
print(format_str)

#-menampilkan tanda + atau -
angka_minus = -28
angka_plus = 28.122005
format_minus = f"Minus= {angka_minus:+d}" #+d plus decimal, udah ada -28 jadi tetep -28
format_plus = f"Plus= {angka_plus:+.2f}"
print("----------------------------------") 
print(format_minus) #normal
print(format_plus)

#-menampilkan persentase
persen = 0.045
format_persen = f"Persen= {persen:.2%}"
print("----------------------------------") 
print(format_persen)

#-aritmatika dalam placeholder
harga = 5000
jumlah = 5
format_str = f"Harga total= Rp. {harga*jumlah:,}"
print("============Aritmatika============")
print(format_str)

#-leading zero
angka = 2005.2912
format_str = f"Angka= {angka:7.2f}" # (.2f) ambil 2 angka belakang koma, f= float
print("===========Leading Zero===========")
print(format_str) #normal

angka = 2005.2912
format_str = f"Angka= {angka:8.2f}" # (.2f) ambil 2 angka belakang koma, f= float
print("----------------------------------") 
print(format_str) #depannya bakal kosong

angka = 2005.2912
format_str = f"Angka= {angka:08.2f}" # (.2f) ambil 2 angka belakang koma, f= float
print("----------------------------------") 
print(format_str) #depannya diisi jadi 0 

#-boolean
boolean = True
format_str = f"Boolean= {boolean}"
print("=============Boolean=============")
print(format_str)

boolean = False
format_str = f"Boolean= {boolean}"
print(format_str) 
