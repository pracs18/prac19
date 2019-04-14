def hex_to_bin(string):
	return format(int(string, 16), '064b')

def bin_to_hex(string):
	return format(int(string, 2), '016x')

def liner():
	print('-'*80)

def at(string, table):
	print(f'Applying {table}')
	retval = []
	for index in [int(v) for v in open(table+'.txt').read().strip().split()]:
		retval.append(string[index-1])
	return ''.join(retval)

def lshift(string, c):
	return string[c:]+string[:c]

def iteration(string):
	print(f'Applying Iterations')
	c = {0: string[:28]}
	d = {0: string[28:]}
	print(f'c0:{c[0]}\nd0:{d[0]}')
	liner()
	it = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

	for i in range(1, 17):
		c[i] = lshift(c[i-1], it[i-1])
		d[i] = lshift(d[i-1], it[i-1])
		print(f'c{i}:{c[i]}\nd{i}:{d[i]}')
		liner()
	
	k = {i:at(c[i]+d[i], 'pc2') for i in range(17)}
	return k

def xor(v1, v2):
	return format(int(v1, 2)^int(v2, 2), '048b')

def s(string):
	st = [int(v) for v in open('s.txt').read().strip().split()]
	retval = []
	for i in range(1, 9):
		ss = string[(i-1)*6:i*6]
		r = int(ss[0]+ss[-1], 2)
		c = int(ss[1:-1], 2)
		retval.append(format(st[((i-1)*4+r)*16 + c], '04b'))
	return ''.join(retval)

def f(rv, kv):
	ev = at(rv, 'e')
	xorv = xor(ev, kv)
	sv = s(xorv)
	fv = at(sv, 'p')
	return fv

if __name__ == '__main__':
	key = hex_to_bin(input())
	plaintext = hex_to_bin(input())
	print(f'key:{key}\nplaintext:{plaintext}')
	liner()

	keyplus = at(key, 'pc1')
	print(f'K+ is {keyplus}\nLength is {len(keyplus)}')
	liner()

	k = iteration(keyplus)
	for key, val in k.items():
		print(f'K{key}:{val}')
	liner()

	ipplaintext = at(plaintext, 'ip')
	print(f'IP:{ipplaintext}')
	liner()

	l = {0:ipplaintext[:32]}
	r = {0:ipplaintext[32:]}
	print(f'l0:{l[0]}\nr0:{r[0]}')
	liner()
	for i in range(1, 17):
		l[i] = r[i-1]
		r[i] = format(int(l[i-1], 2) + int(f(r[i-1], k[i]), 2), '032b')
		print(f'l{i}:{l[i]}\nr{i}:{r[i]}')
		liner()
	
	cipher = at(r[16]+l[16], 'ipinv')
	print(f'Cipher:{cipher}')
	cipher = bin_to_hex(cipher)
	print(f'Cipher:{cipher}')