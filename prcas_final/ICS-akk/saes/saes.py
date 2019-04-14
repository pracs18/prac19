#######################
# Author: Aditya Khadse
# Roll no: BECOA166
#######################
SBOX = '1001 0100 1010 1011 1101 0001 1000 0101 0110 0010 0000 0011 1100 1110 1111 0111'.split(' ')
R = '1000 0011'.split(' ')

def hex_to_bin(string):
    return format(int(string, 16), '016b')

def hex_to_4bin(string):
    return format(int(string, 16), '04b')

def xor(s1, s2):
    ans = []
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            ans.append('0')
        else:
            ans.append('1')
    return ''.join(ans)

def s(w):
    print(f's: {int(w, 2)} {SBOX[int(w, 2)]}')
    return SBOX[int(w, 2)]

def g(w, rn):
    n0, n1 = w[:4], w[4:]
    
    #Rotate Word
    n0, n1 = n1, n0 

    #Sub word
    n0 = s(n0)
    n1 = s(n1)

    #Round constant
    r = R[rn-1]
    n0 = xor(n0, r)
    n1 = xor(n1, '0000')

    return n0 + n1

def expand_key(w0, w1, rn):
    gv = g(w1, rn)
    w2 = xor(w0, gv)
    w3 = xor(w2, w1)
    return w2, w3

def mix_columns(s00, s01, s10, s11):
    lookup = [line.split(' ') for line in open('lookup.txt').readlines()]
    s00n = xor(s00, hex_to_4bin(lookup[4][int(s10, 2)]))
    s10n = xor(hex_to_4bin(lookup[int(s00, 2)][4]), s10)
    s01n = xor(s01, hex_to_4bin(lookup[4][int(s11, 2)]))
    s11n = xor(hex_to_4bin(lookup[int(s01, 2)][4]), s11)
    return s00n,s01n,s10n,s11n

# def mix_columns(s00, s01, s10, s11):
    # b0, b1, b2, b3 = s00
    # b4, b5, b6, b7 = s10
    # c0, c1, c2, c3 = s01
    # c4, c5, c6, c7 = s11

    # s00 = xor(b0, b6) + \
    #         xor(b1, xor(b4, b7)) + \
    #         xor(b2, xor(b4, b5)) + \
    #         xor(b3, b5)

    # s10 = xor(b2, b4) + \
    #         xor(b0, xor(b3, b5)) + \
    #         xor(b0, xor(b1, b6)) + \
    #         xor(b1, b7)

    # s10 = xor(c0, c6) + \
    #         xor(c1, xor(c4, c7)) + \
    #         xor(c2, xor(c4, c5)) + \
    #         xor(c3, c5)

    # s11 = xor(c2, c4) + \
    #         xor(c0, xor(c3, c5)) + \
    #         xor(c0, xor(c1, c6)) + \
    #         xor(c1, c7)

    # return s00, s01, s10, s11

def encrypt(text, key):
    text = xor(text, key)
    
    w0 = key[0:4] + key[4:8]
    w1 = key[8:12] + key[12:16]

    # Expand Key
    w2, w3 = expand_key(w0, w1, 1)

    # Substitute
    s00 = s(text[0:4])
    s10 = s(text[4:8])
    s01 = s(text[8:12])
    s11 = s(text[12:16])

    # Shift Rows
    s10, s11 = s11, s10

    # Mix Columns
    s00, s01, s10, s11 = mix_columns(s00, s01, s10, s11)
    print(s00, s01, s10, s11)

    # Add Round Key
    text = xor(s00+s10+s01+s11, w2+w3)

    # Expand Key
    w4, w5 = expand_key(w2, w3, 2)

    # Substitute
    s00 = s(text[0:4])
    s10 = s(text[4:8])
    s01 = s(text[8:12])
    s11 = s(text[12:16])

    #Shift Rows
    s10, s11 = s11, s10

    # Add Round Key
    text = xor(s00+s01+s10+s11, w4+w5)

    return text

plaintext = input('Enter 16 bit plaintext: ')
key = input('Enter 16 bit key: ')

# key = hex_to_bin(input('Enter 16 bit key in hex: '))
# plaintext = hex_to_bin(input('Enter 16 bit plaintext in hex: '))

print('Cipher:', encrypt(plaintext, key))