#######################
# Author: Aditya Khadse
# Roll no: BECOA166
#######################
from primes import random_prime

q = random_prime()

def check_if_primitive_root(q, r):
    mods = set(range(1, q))
    powerv = 1
    for i in range(1, q):
        powerv *= r
        v = powerv % q
        if v in mods:
            mods.remove(v)
        else:
            return False
    if len(mods) == 0:
        return True
    else:
        return False

r = None
for i in range(2, q):
    if check_if_primitive_root(q, i):
        r = i
        break

xa = int(input('Enter private key of A: '))
xb = int(input('Enter private key of B: '))

ya = (r**xa) % q
yb = (r**xb) % q

print(f'Public key of A is {ya}')
print(f'Public key of B is {yb}')

k = (ya ** xb) % q
print(f'Secret key is {k}')