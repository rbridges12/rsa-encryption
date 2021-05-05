

def encrypt_list(msg, n, e):
    return [((c + 100) ** e) % n for c in msg.encode('ASCII')]

def decrypt_list(cipher_list, n, d):
    codes = [((c ** d) % n) - 100 for c in cipher_list]
    msg = bytes(codes).decode('ASCII')
    return msg
 

def encrypt(msg, n, e):
    digits = int(''.join([str(c + 100) for c in msg.encode('ASCII')]))
    print(digits)
    cipher_text = (digits ** e) % n
    return cipher_text


def decrypt(cipher_text, n, d):
    t1 = str((cipher_text ** d) % n)
    print(t1)
    codes = [int(t1[n:n+3]) - 100 for n in range(0, len(t1), 3)]
    print(codes)
    msg = bytes(codes).decode('ASCII')
    return msg


with open('keys.txt', 'r') as keys:
    n, e, d = tuple(int(key[:-1]) for key in list(keys))

print('n = %d\ne = %d\nd = %d' % (n, e, d))

msg = input('enter message: ')
code = encrypt(msg, n, e)
print('encrypted message: ')
print(code)
decrypted = decrypt(code, n, d)
print('decrypted message: %s' % decrypted)
