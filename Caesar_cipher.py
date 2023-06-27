# https://hanco.tistory.com/2

def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 64
        t = a + k
        if t > 90: t -= 27
        if t == 64: t = 32
        c += chr(t)
    return c

def decipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 91
        t = a - k
        if t < 65: t += 27
        if t == 91: t = 32
        c += chr(t)
    return c

plainText = 'APPLE BANANA'
k = 1
print('평 문 : ', plainText)
cipherText = encipher(plainText, k)
print('암호문 : ', cipherText)
print('복호문 : ', decipher(cipherText, k))