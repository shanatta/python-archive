#Operator Bitwise

#operator bitwise, operasi biner, binary
#bitwise (operasi pada masing masing bit)
#int ke biner
#int 9= 00001001
#2^3+2^0= 9

a = 9
b = 5

#-bitwise OR (|)
c = a | b
print('\n==============OR==============')
print('nilai: ',a,', binary: ',format(a,'08b'))
print('nilai: ',b,', binary: ',format(b,'08b'))
print('------------------------------ (|)')
print('nilai: ',c,', binary: ',format(c,'08b'))

#-bitwise AND (&)
c = a & b
print('\n==============AND==============')
print('nilai: ',a,', binary: ',format(a,'08b'))
print('nilai: ',b,', binary: ',format(b,'08b'))
print('------------------------------ (&)')
print('nilai: ',c,', binary: ',format(c,'08b'))

#-bitwise XOR (^)
c = a ^ b
print('\n==============XOR==============')
print('nilai: ',a,', binary: ',format(a,'08b'))
print('nilai: ',b,', binary: ',format(b,'08b'))
print('------------------------------ (^)')
print('nilai: ',c,', binary: ',format(c,'08b'))

#-bitwise NOT (~)
c = ~a 
print('\n==============NOT==============')
print('nilai: ',a,', binary: ',format(a,'08b'))
print('------------------------------ (~)')
print('nilai: ',c,', binary: ',format(c,'08b'))
print('------------------------------ (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai: ',e^d,', binary: ',format(e^d,'08b'))

#shifting 
#-shift right (>>)
c = a >> 2
print('\n==========shift right==========')
print('nilai: ',a,', binary: ',format(a,'08b'))
print('------------------------------ (>>)')
print('nilai: ',c,', binary: ',format(c,'08b'))

#-shift right (<<)
c = a << 2
print('\n===========shift left===========')
print('nilai: ',a,', binary: ',format(a,'08b'))
print('------------------------------ (<<)')
print('nilai: ',c,', binary: ',format(c,'08b')) 
