
def isprimitiveroot(q,a):
	return sorted([(a**i)%q for i in range(1,q)]) == list(range(1,q))

q = int(input("Enter a prime no: ") )
while True : 
	a = int( input("Enter its primitive root : ") ) 
	if isprimitiveroot(q,a) :
		break
	print(a,"is not primitive root of",q)
	print("Please Enter again") 

xA =  int(input("Enter private key of A:") )
yA =  (a**xA) % q 

xB =  int(input("Enter private key of B:") )
yB =  (a**xB) % q 

#Calculation of Secret Key by user A
kA =  (yB**xA) % q 

#Calculation of Secret Key by user B
kB =  (yA**xB) % q 

print("Public key of A:",yA)
print("Private key of B:",yB)

print("Key calculated at A side:",kA)
print("Key calculated at B side:",kB)

'''
Sample Input: 

Enter a prime no: 353
Enter its primitive root : 3
Enter private key of A:97
Enter private key of B:233
Public key of A: 40
Private key of B: 248
Key calculated at A side: 160
Key calculated at B side: 160
'''
