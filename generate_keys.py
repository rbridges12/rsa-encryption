import random

# TODO: random seed argument
# TODO: dont hardcode
def generate_keys():
    # p = 30781
    # q = 58913
    p = 13
    q = 41
    n = p * q
    phi = (p-1) * (q-1)
    e = coprime(phi)
    d = gcd(e, phi)[1]
    
    with open('keys.txt', 'w') as f:
        f.write("%d\n%d\n%d\n" %(n, e, d))



# TODO: timeout
def coprime(phi):
    while True:
        r = random.randrange(2, phi)
        if gcd(r, phi)[0] == 1:
            return r

def gcd(a, b):
    r1 = a
    r2 = b
    u1 = 1
    v1 = 0
    u2 = 0
    v2 = 1
    
    # TODO: pythonic updates
    while r2 != 0:
        q = r1 // r2
        r3 = r1
        u3 = u1
        v3 = v1
        r1 = r2
        u1 = u2
        v1 = v2
        r2 = r3 - q * r2
        u2 = u3 - q * u2
        v2 = v3 - q * v2

    return (r1, u1, v1)

generate_keys()