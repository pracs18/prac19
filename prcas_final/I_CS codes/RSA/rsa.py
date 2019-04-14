from math import *
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
	
def modularInverse(e,phiN):
	k = 1 
	while (phiN*k + 1)%e !=0 : 
		k+=1 
	return (phiN*k+1)//e 

p = int(input("Enter prime no 1:"))
q = int(input("Enter prime no 2:"))
n = p * q 
phiN = (p-1) * (q-1)

for num in range(2,phiN):
	if gcd(num,phiN) == 1: 
		e = num
		break
print("Public key for encryption",e)
d = modularInverse(e,phiN)
print("Public key for decryption",d)
m = int(input("Enter message:"))
c = m**e%n
print("Cipher after encryption:" , c) 

dm = c**d%n
print("Orig message after decrytpion:",dm)

'''
Enter a prime no: 353
Enter its primitive root : 3
Enter private key of A:97
Enter private key of B:233
Public key of A 40
Private key of B 248
Key calculated at A side 160
Key calculated at B side 160
'''
