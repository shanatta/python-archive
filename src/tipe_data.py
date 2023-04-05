#Tipe data

data_integer = 28 #integer
print("Data=", data_integer, "bertipe", type(data_integer)) 

data_float = 16.5 #float (ada koma)
print("Data=", data_float, "bertipe", type(data_float)) 

data_string = "Aizen 8" #string
print("Data=", data_string, "bertipe", type(data_string)) 

data_bool = True #boolean
print("Data=", data_bool, "bertipe", type(data_bool)) 

#-tipe data khusus
data_complex = complex(5, 6) #complex
print("Data=", data_complex, "bertipe", type(data_complex)) 

#-tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(29.5) #c double
print("Data=", data_c_double, "bertipe", type(data_c_double)) 
