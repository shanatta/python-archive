#Komparasi dan logika

#membuat gabungan area rentang dari angka
#+++++++3-----10++++++++++
inputUser = float(input("Masukan angka kurang dari 3 atau lebih dari 10: "))

#+++++3 
#-memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("===========================\nKurang dari 3=", inputUser, "is", isKurangDari)

#10+++++
#-memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10=", inputUser, "is", isLebihDari)

#+++++++3-----10++++++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yg anda masukan:", isCorrect) 
