#Operasi dan Manipulasi String

#-menyambung string (concatenate)
nama_pertama = "Rey"
nama_akhir = " Miyuki"
nama_lengkap = nama_pertama + nama_akhir
print("===========Sambung String===========")
print(nama_lengkap)

#-menghitung panjang string 
panjang = len(nama_lengkap)
print("===========Panjang String===========")
print("Panjang dari " + nama_lengkap + "= " + str(panjang) + " (termasuk spasi)")

#-cek komponen char/string di string
R = "R"
status = R in nama_lengkap
print("=============Cek String=============")
print(R + " di " + nama_lengkap + "= " + str(status))

r = "r"
status = r in nama_lengkap
print(r + " di " + nama_lengkap + "= " + str(status))

r = "r"
status = r not in nama_lengkap
print(r + " tidak ada di " + nama_lengkap + "= " + str(status))

#-mengulang string
print("============Ulang String============")
print("wk"*5)
print(5*"wk") 

#-indexing
print("==============Indexing==============")
print("index ke-0= " + nama_lengkap[0])
print("index ke-1= " + nama_lengkap[1])
print("index ke-(-1)= " + nama_lengkap[-1]) #dari belakang -1
print("index ke-(-2)= " + nama_lengkap[-2])
print("index ke-(0:2)= " + nama_lengkap[0:3]) #range #=index 0-2
print("index ke-(4:10)= " + nama_lengkap[4:11]) #range #=index 4-10
print("index ke-(0, 2, 4, 6, 8)= " + nama_lengkap[0:8:2]) #range increment 2 

#-item paling kecil (min)
print("================Min================")
print("Item paling kecil= " + min(nama_lengkap)) #kosong/spasi

#-item paling besar (max)
print("================Max================")
print("Item paling besar= " + max(nama_lengkap))

#-ASCII code
ascii_code = ord(" ")
print("=============ASCII Code=============")
print("ASCII code untuk spasi= " + str(ascii_code))

ascii_code = ord("'")
print("ASCII code untuk tanda kutip= " + str(ascii_code))

data = 117
print("Char untuk ASCII= " + chr(data))

#operator dalam bentuk method 
#-count
data = "sigit rendang"
jumlah =  data.count("i")
print("===============Count===============")
print("Jumlah i pada " + data + "= " + str(jumlah))

#-upper case
salam = "hello!"
print("============Upper Case============")
print("Salam= " + salam)
salam = salam.upper()
print("Upper= " + salam)

#-lower case
salam = "ApA KabAR?"
print("============Lower Case============")
print("Salam= " + salam)
salam = salam.lower()
print("Lower= " + salam)

#isX method
#-is lower
salam = "bang"
apakah_lower = salam.islower() #hasilnya boolean
print("==============Is Lower==============")
print(salam + " is lower= " + str(apakah_lower))

#-is upper
salam = "bang"
apakah_upper = salam.isupper() #hasilnya boolean
print("==============Is Upper==============")
print(salam + " is upper= " + str(apakah_upper))

#-is alpha (cek huruf)
huruf = "012345"
cek_huruf = huruf.isalpha() #hasil boolean
print("==============Is Alpha==============")
print(huruf + " is alpha= " + str(cek_huruf))

huruf = "abcde"
cek_huruf = huruf.isalpha() #hasil boolean
print(huruf + " is alpha= " + str(cek_huruf))

huruf = "abc123"
cek_huruf = huruf.isalpha() #tetep ada angkanya= false
print(huruf + " is alpha= " + str(cek_huruf))

#-is alnum (cek huruf & angka)
kata = "012345"
cek_kata = kata.isalnum() #hasil boolean
print("==============Is Alnum==============")
print(kata + " is alnum= " + str(cek_kata))

kata = "abcde"
cek_kata = kata.isalnum() #hasil boolean
print(kata + " is alnum= " + str(cek_kata))

kata = "abc123"
cek_kata = kata.isalnum() #hasil boolean
print(kata + " is alnum= " + str(cek_kata))

kata = "abc#123"
cek_kata = kata.isalnum() #hasil ada tandanya= false
print(kata + " is alnum= " + str(cek_kata))

#-is decimal (cek angka)
angka = "012345"
cek_angka = angka.isdecimal() #hasil boolean
print("==============Is Decimal==============")
print(angka + " is decimal= " + str(cek_angka))

angka = "abcde"
cek_angka = angka.isdecimal() #hasil boolean
print(angka + " is decimal= " + str(cek_angka))

angka = "abc123"
cek_angka = angka.isdecimal() #ada hurufnya= false
print(angka + " is decimal= " + str(cek_angka))

angka = "#123"
cek_angka = angka.isdecimal() #ada tandanya= false
print(angka + " is decimal= " + str(cek_angka))

#-is space (cek spasi, tab, newline, \n)
kata = " a "
cek_kata = kata.isspace() #false karena ada hurufnya
print("==============Is Space==============")
print(kata + " is space= " + str(cek_kata))

kata = " " 
cek_kata = kata.isspace() #true karena " kosong "
print("----------------------------------")
print(kata + " is space= " + str(cek_kata))

kata = "" 
cek_kata = kata.isspace() #false 
print("----------------------------------")
print(kata + " is space= " + str(cek_kata))

kata = "\r \n"
cek_kata = kata.isspace() #true (simbol \r, \n doang)
print("----------------------------------")
print(kata + " is space= " + str(cek_kata))

kata = "a\nbc123"
cek_kata = kata.isspace() #false ada katanya
print("----------------------------------")
print(kata + " is space= " + str(cek_kata))

#-is title (huruf kapital di awal)
judul = "Its Okay Not TO BE Okay"
cek_judul = judul.istitle() #false karena besar kecil 
print("==============Is Title==============")
print(judul + " is title= " + str(cek_judul))

judul = "It's okay not to be okay"
cek_judul = judul.istitle() #false karena ada tanda petiknya
print("----------------------------------")
print(judul + " is title= " + str(cek_judul))

judul = "Its Okay Not To Be Okay"
cek_judul = judul.istitle() #hasil true
print("----------------------------------")
print(judul + " is title= " + str(cek_judul))

#-startswith 
cek_start = "Azeril Baihaqy".startswith("Azeril")
print("============Starts With============")
print("Start= " + str(cek_start))

cek_start = "Azeril Baihaqy".startswith("azeril")
print("Start= " + str(cek_start))

#-endswith
cek_end = "Azeril Baihaqy".endswith("Baihaqy")
print("=============Ends With=============")
print("Ends= " + str(cek_end))

cek_end = "Azeril Baihaqy".endswith("baihaqy")
print("Ends= " + str(cek_end))

#penggabungan komponen
#-join()
pisah = ['aku', 'cina', 'jawa']
gabungan = ','.join(pisah)
print("===============Join===============")
print(pisah) #normal 
print("----------------------------------")
print(gabungan) #jadi aku,cina,jawa (, nya tetep ikut join)
print("----------------------------------")

gabungan = ''.join(pisah)
print(gabungan) #jadi akucinajawa  
gabungan = ' ee '.join(pisah)
print("----------------------------------")
print(gabungan) #jadi aku ee cina ee jawa
print("----------------------------------")

#-split()
gabungan = "akueecinaeejawa"
print("==============Split==============")
print(gabungan.split('ee')) #jadi ['aku', 'cina', 'jawa']
print("----------------------------------")

#alokasi karakter
#-rjust()
kanan = "kanan".rjust(10)
print("=============R Just=============")
print("'" + kanan + "'") #spasi di kanan

#-ljust()
kiri = "kiri".ljust(10)
print("=============L Just=============")
print("'" + kiri + "'") #spasi di kiri

#-center()
tengah = "tengah".center(10, "0") #yang kosong diisi 
print("=============Center=============")
print("'" + tengah + "'") #diberi jarak 10, dan tulisan jadi di tengah

#strip()
tengah = tengah.strip("0")
print("==============Strip==============")
print("'" + tengah + "'") #menghilangkan tanda 0 
