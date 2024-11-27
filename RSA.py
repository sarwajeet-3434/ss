import math


def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a


def mod_inverse(e, phi):
    
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None  


p = 3
q = 7
n = p * q
e = 2
phi = (p - 1) * (q - 1)


while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1


d = mod_inverse(e, phi)


print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")


msg = 12
print(f"Original message: {msg}")


c = pow(msg, e, n)
print(f"Encrypted message: {c}")
