import random
from hashlib import sha1

def generate_keys():
    q = 23
    p = 383
    h = 2
    g = pow(h, (p - 1) // q, p)
    x = random.randint(1, q - 1)
    y = pow(g, x, p)
    public_key = (p, q, g, y)
    private_key = (p, q, g, x)
    return public_key, private_key

def sign_message(private_key, message):
    p, q, g, x = private_key
    h = int(sha1(message.encode()).hexdigest(), 16)
    while True:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = pow(k, -1, q)
        s = (k_inv * (h + r * x)) % q
        if s != 0:
            break
    return (r, s)

def verify_signature(public_key, message, signature):
    p, q, g, y = public_key
    r, s = signature
    h = int(sha1(message.encode()).hexdigest(), 16)
    if not (0 < r < q and 0 < s < q):
        return False
    w = pow(s, -1, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    V = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return V == r

public_key, private_key = generate_keys()
message = "Hello, DSA!"
signature = sign_message(private_key, message)
is_valid = verify_signature(public_key, message, signature)

print("Message:", message)
print("Signature:", signature)
print("Is the signature valid?", is_valid)
