import os
from random import choice

def generate_primes(n=200, primes=[2, 3]):
    if n > primes[-1]:
        for number in range(primes[-1]+1, n+1):
            for prime in primes:
                if number % prime == 0:
                    break
            else:
                primes.append(number)
    with open('primes.txt', 'w') as f:
        for prime in primes:
            f.write(str(prime)+'\n')
    return primes

PRIMES = list(map(int, open('primes.txt').readlines())) if os.path.isfile('primes.txt') else generate_primes()

def random_prime():
    return choice(PRIMES[2:])

if __name__ == '__main__':
    print('Primes are:', *PRIMES)