#Casting tipe data (konversi tipe data)

#-integer
print("====Integer====")
data_int = 9;
print("Data=", data_int, "type=", type(data_int))

data_float = float(data_int)
data_bool = bool(data_int)
data_str = str(data_int) #false jika int=0

print("Data=", data_float, "type=", type(data_float))
print("Data=", data_bool, "type=", type(data_bool))
print("Data=", data_str, "type=", type(data_str))

#-float
print("====Float====")
data_float = 9.5;
print("Data=", data_float, "type=", type(data_float))

data_bool = bool(data_float) #dibulatkan ke bawah
data_str = str(data_float)
data_int = int(data_float) #false jika float=0

print("Data=", data_int, "type=", type(data_int))
print("Data=", data_str, "type=", type(data_str))
print("Data=", data_bool, "type=", type(data_bool))

#-boolean
print("====Boolean====")
data_bool = False;
print("Data=", data_bool, "type=", type(data_bool))

data_str = str(data_bool) #dibulatkan ke bawah
data_int = int(data_bool)
data_float = float(data_bool) #false jika float=0

print("Data=", data_str, "type=", type(data_str))
print("Data=", data_int, "type=", type(data_int))
print("Data=", data_float, "type=", type(data_float))

#-string
print("====String====")
data_str = "10"; #string harus angka jika ingin di konvers ke int
print("Data=", data_str, "type=", type(data_str))

data_int = int(data_str) 
data_float = float(data_str) #false jika string kosong
data_bool = bool(data_str) 

print("Data=", data_int, "type=", type(data_int))
print("Data=", data_float, "type=", type(data_float))
print("Data=", data_bool, "type=", type(data_bool)) 
