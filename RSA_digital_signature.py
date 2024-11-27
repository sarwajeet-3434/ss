# Function to find gcd of two numbers using Euclid's algorithm
def euclid(m, n):
    if n == 0:
        return m
    else:
        return euclid(n, m % n)

# Function to find the multiplicative inverse using Extended Euclidean Algorithm
def exteuclid(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r
        s = s1 - q * s2
        s1, s2 = s2, s
        t = t1 - q * t2
        t1, t2 = t2, t
    
    if t1 < 0:
        t1 = t1 % a
    
    return (r1, t1)

# Main program starts here
# Large prime numbers p and q
p = 823
q = 953

# Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Generate encryption keys in range 1 < e < phi(n) such that gcd(e, phi_n) = 1
key = []
for i in range(2, phi_n):
    gcd = euclid(phi_n, i)
    if gcd == 1:
        key.append(i)

# Select an encryption key
e = 313  # Example encryption key

# Calculate the decryption key (multiplicative inverse of e modulo phi_n)
r, d = exteuclid(phi_n, e)
if r == 1:
    d = int(d)
    print("Decryption key is:", d)
else:
    print("Multiplicative inverse for the given encryption key does not exist. Choose a different encryption key.")
    exit()

# Enter the message to be sent
M = 19070  # Ensure M < n
if M >= n:
    print("Message too large for encryption. Choose a smaller message.")
    exit()

# Signature is created by Alice
S = pow(M, d, n)

# Alice sends M and S to Bob
# Bob verifies the signature
M1 = pow(S, e, n)

# Verification
if M == M1:
    print("As M = M1, Accept the message sent by Alice.")
else:
    print("As M != M1, Do not accept the message sent by Alice.")
