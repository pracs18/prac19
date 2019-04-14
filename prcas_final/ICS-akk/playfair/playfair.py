##########################
#   Author: Aditya Khadse
#   Roll No: BECOA166
##########################

from string import ascii_uppercase as letters
letters = letters.replace('J', '')

def remove_repeat(string):
    charset = set()
    ans = []
    for c in string:
        if c not in charset:
            ans.append(c)
        charset.add(c)
    
    return ''.join(ans)

def remove_punctuation(string):
    punctuations = [
        '.', ',', "'",
        '"', '!', '?', ' '
    ]
    for p in punctuations:
        string = string.replace(p, '')

    return string

def create_matrix(key):
    key.replace('J', 'I')
    key.replace('j', 'I')
    key = remove_repeat(key.upper()+letters)
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def find_in_matrix(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_pair(a, b, matrix):
    if a == b:
        b = 'X'
    r1, c1 = find_in_matrix(a, matrix)
    r2, c2 = find_in_matrix(b, matrix)

    if r1 == r2:
        return matrix[r1][(c1+1)%5], matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1], matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2], matrix[r2][c1]

def decrypt_pair(a, b, matrix):
    r1, c1 = find_in_matrix(a, matrix)
    r2, c2 = find_in_matrix(b, matrix)

    if r1 == r2:
        return matrix[r1][(c1-1)%5], matrix[r2][(c2-1)%5]
    elif c1 == c2:
        return matrix[(r1-1)%5][c1], matrix[(r2-1)%5][c2]
    else:
        return matrix[r1][c2], matrix[r2][c1]

def encipher(text, key):
    matrix = create_matrix(key)
    text = remove_punctuation(text.upper())
    if len(text) % 2 != 0:
        text = text + 'X'
    ans = []
    for i in range(0, len(text), 2):
        ans.extend(list(encrypt_pair(text[i], text[i+1], matrix)))
    return ''.join(ans)

def decipher(text, key):
    matrix = create_matrix(key)
    ans = []
    for i in range(0, len(text), 2):
        ans.extend(list(decrypt_pair(text[i], text[i+1], matrix)))
    return ''.join(ans)

if __name__ == '__main__':
    key = input('Enter key: ')
    text = input('Enter plaintext: ')
    ciphertext = encipher(text, key)
    print('Encrypted in Playfair: {}'.format(ciphertext))
    decrypted = decipher(ciphertext, key)
    print('Decrypted in Playfair: {}'.format(decrypted))