#Kalkulator sederhana

#-program konversi celcius ke satuan lain
print("\nProgram Konversi Temperatur\n")

celcius = float(input("Masukan suhu dalam celcius: "))
print("Suhu:", celcius, "Celcius")

#-celcius-reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur:", reamur, "R")

#-celcius-fahrenheit
fahrenheit = ((9/5) * celcius)  + 32
print("Suhu dalam fahrenheit:", fahrenheit, "F")

#-celcius-kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin:", reamur, "K")


#-fahrenheit-kelvin (latihan)
fahrenheit = float(input("====Fahrenheit - Kelvin====\nMasukan suhu dalam fahrenheit:"))
print("Suhu:", fahrenheit, "Fahrenheit")

kelvin = (((5/9) * (fahrenheit - 32)) + 273)
print("Suhu dalam kelvin:", kelvin, "K")

#-kelvin-fahrenheit (latihan)
kelvin = float(input("====Kelvin - Fahrenheit====\nMasukan suhu dalam kelvin: "))
print("Suhu:", kelvin, "Kelvin")

#-kelvin-ceelcius dulu
celcius = kelvin - 273
print("Suhu dalam celcius:", celcius, "C")

#-lalu celcius-fahrenheit 
fahrenheit = ((9/5) * celcius)  + 32
print("Suhu dalam fahrenheit:", fahrenheit, "F") 
