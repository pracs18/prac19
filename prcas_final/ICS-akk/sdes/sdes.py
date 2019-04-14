#########################
# Author: Aditya Khadse
# Roll no: BECOA166
#########################

def at(string, table):
	print('Applying {}'.format(table))
	retval = []
	for index in [int(v) for v in open(table+'.txt').read().strip().split()]:
		retval.append(string[index-1])
	return ''.join(retval)

def lshift(string, k):
	return string[k:] + string[:k]

def s0(s):
	r = int(s[0]+s[-1], 2)
	c = int(s[1:-1], 2)
	table = [
		[1, 0, 3, 2],
		[3, 2, 1, 0],
		[0, 2, 1, 3],
		[3, 1, 3, 2]
	]
	return format(table[r][c], '02b')
	
def s1(s):
	r = int(s[0]+s[-1], 2)
	c = int(s[1:-1], 2)
	table = [
		[0, 1, 2, 3],
		[2, 0, 1, 3],
		[3, 0, 1, 0],
		[2, 1, 0, 3]
	]
	return format(table[r][c], '02b')
	
def xor(s1, s2):
	retval = []
	for v1, v2 in zip(s1, s2):
		if v1 == v2:
			retval.append('0')
		else:
			retval.append('1')
	return ''.join(retval)

def sw(string):
	return string[4:], string[:4]

def keygen(key):
	kplus = at(key, 'p10')
	l = kplus[:5]
	r = kplus[5:]
	k1 = at(lshift(l, 1) + lshift(r, 1), 'p8')
	k2 = at(lshift(l, 3) + lshift(r, 3), 'p8')
	return k1, k2

def apply_round(text, key):
	lp = text[:4]
	rp = text[4:]
	rpe = at(rp, 'ep')
	xorv = xor(key, rpe)
	sv = s0(xorv[:4]) + s1(xorv[4:])
	svp = at(sv, 'p4')
	xorsv = xor(lp, svp)
	return xorsv, rp

def f(p, k):
	v = at(p, 'ep')
	v = xor(v, k)
	l, r = v[:4], v[4:]
	v = at(s0(l)+s1(r), 'p4')
	return v 

def fk(l, r, k):
	return xor(l, f(r, k)), r
	
if __name__ == '__main__':
	plain_text = input('Plain text in binary(8 bits): ')
	key = input('Key in binary(8 bits): ')
	k1, k2 = keygen(key)
	print(k1, k2)
	
	iptext = at(plain_text, 'ip')
	print('iptext', iptext)
	l, r = fk(iptext[:4], iptext[4:], k1)
	l, r = sw(l+r)
	print('round 1:', l, r)
	l, r = fk(l, r, k2)
	print('round 2:', l, r)
	cipher = at(l+r, 'ipinv')
	
	print('Cipher is:', cipher)
	
	
	
	
	
	
	
	
	
	
