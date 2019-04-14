key = input("Enter the key without spaces:") + ''.join([chr(ch+ord('a')) for ch in range(26) ])
key = key.replace('j','i')
used = ""
pm = []
for ch in key:
	if ch not in used:
		pm.append(ch)
		used+=ch
pm = [ pm[i:i+5] for i in range(0,25,5) ] 
print("\nPlayFair Matrix:")
print(*pm,sep='\n')

def encrypt(s):
	pos = [[i,j] for i in range(5) for j in range(5) if s[0] in pm[i][j] ] 
	x1,y1 = pos[0][0],pos[0][1]
	pos = [[i,j] for i in range(5) for j in range(5) if s[1] in pm[i][j]  ] 
	x2,y2 = pos[0][0],pos[0][1]
	if x1 == x2 : 
		return pm[x1][(y1+1)%5]+pm[x2][(y2+1)%5]
	if y1 == y2 : 
		return pm[(x1+1)%5][y1]+pm[(x2+1)%5][y2]
	return pm[x1][y2] + pm[x2][y1]

pt = input("\nEnter the plaintext:")
pt = pt.replace('j','i')
for ch in ", ;.":
	pt = pt.replace(ch,'')
l = len(pt)
i=0
while i < (l-1) : 
	if pt[i] == pt[i+1] : 
		pt = pt[:i+1] + 'x' + pt[i+1:]
		l+=1
	i+=2
if l%2:
	pt+='x'
	l+=1
paired_pt = " ".join([pt[i:i+2] for i in range(0,l,2) ])
print("\nPlaintext in paired form:",paired_pt)
cipher = ""

for i in range(0,l,2):
	cipher+=encrypt(pt[i]+pt[i+1])

print("\nEncrypted text:",cipher)

'''
Sample Input:

Enter the key without spaces:another

PlayFair Matrix:
['a', 'n', 'o', 't', 'h']
['e', 'r', 'b', 'c', 'd']
['f', 'g', 'i', 'k', 'l']
['m', 'p', 'q', 's', 'u']
['v', 'w', 'x', 'y', 'z']

Enter the plaintext:we live in a world full of beauty

Plaintext in paired form: we li ve in aw or ld fu lx lo fb ea ut yx

Encrypted text: vrfkafgonvnbullmizihiefeshzy
'''


