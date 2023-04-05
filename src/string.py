#String

data = "Kaori Miyazono"
print(data)
print(type(data))

#-menggunakan single quote (' ')
data = 'Arima Kousei'
print("=======Menggunakan Single Quote=======")
print(data)
print('"Hello Kaori"')

#-menggunakan double quote (" ")
data = "Your Lie in April"
print("=======Menggunakan Double Quote=======")
print(data)
print("'Mozart’s telling us from up the sky… Go on a journey'")

#-menggunakan tanda (\)
print("========Menggunakan Tanda (\)========")
print('jum\'at')
print('g\'day, isn\'t it?')

#-backlash
print("==============Backlash==============")
print("E:\\Cicak\\Love")

#-tab
print("================Tab================")
print("What \tTry") #jauhan teks nya
print("What \t\tTry") #semakin jauh

#-backspace
print("=============Backspace=============")
print("Apa \bCoba") #ga terlalu penting kayaknya
print("ApaCoba") 

#-newline
print("==============Newline==============")
print("Azuru. \nBaik.") #lf (line feed) (untuk unix, mac os, linux)
print("-----------------------------------")

print("Azuru. \rBaik.") #cr (carriage return) (untuk commodore, acorn, lisp)
print("-----------------------------------")

print("Azuru. \r\nBaik.") #crlf (line feed carriage return) (untuk windows)

#-string literal & raw
print("============Raw String============")
print('E:\\newcicak') #double slash rumit (\\)
print(r'E:\new\r\b\cicak') #raw string

#-multiline literal string
print("==========Literal String==========")
print("""
Nama: Azeril
Kelas: TEKAJE
""")

#-multiline literal & raw string
print("=======Literal & Raw String=======") #ada r nya, tag kebaca
print(r""" 
Nama: Azeril
Kelas: esempe \normal
Website: www.cina.com/newID
#bangtkj
""") 
