################
# Author: Aditya Khadse
# Roll no: BECOA166
################

from math import gcd
from primes import random_prime

p = random_prime()
q = random_prime()

n = p * q
phi_n = (p - 1) * (q - 1)

e = None
for i in range(2, phi_n):
    if gcd(i, phi_n) == 1:
        e = i
        break

d = None
i = 1
while (phi_n*i) % e != 0:
    i += 1
d = (phi_n*i) // e

print(f'Generated - p:{p}, q:{q}, e:{e}')

def encrypt(m):
    c = (m**e) % n
    return c

def decrypt(c):
    m = (c**d) % n
    return m

if __name__ == '__main__':
    print('''
    RSA Algorithm
    1. Encrypt
    2. Decrypt
    ''')
    choice = int(input('Enter choice: '))
    if choice == 1:
        m = int(input('Enter plaintext number: '))
        print(f'Cipher is {encrypt(m)}')
    elif choice == 2:
        c = int(input('Enter cipher number: '))
        print(f'Plaintext is {decrypt(c)}')