import numpy as np

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, m):
    det = int(np.round(np.linalg.det(matrix))) % m
    det_inv = mod_inverse(det, m)
    if det_inv is None:
        return None
    matrix_adj = np.round(np.linalg.inv(matrix) * det).astype(int) % m
    return (det_inv * matrix_adj) % m

def hill_encrypt(plain_text, key_matrix):
    m = len(key_matrix)
    plain_text = plain_text.replace(" ", "").upper()
    while len(plain_text) % m != 0:
        plain_text += 'X'
    plain_text_nums = [ord(char) - 65 for char in plain_text]
    cipher_text = ''
    for i in range(0, len(plain_text_nums), m):
        block = np.array(plain_text_nums[i:i + m]).reshape(m, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        cipher_text += ''.join([chr(int(encrypted_block[i][0]) + 65) for i in range(m)])
    return cipher_text

def hill_decrypt(cipher_text, key_matrix):
    m = len(key_matrix)
    cipher_text_nums = [ord(char) - 65 for char in cipher_text]
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    if key_matrix_inv is None:
        return None
    plain_text = ''
    for i in range(0, len(cipher_text_nums), m):
        block = np.array(cipher_text_nums[i:i + m]).reshape(m, 1)
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        plain_text += ''.join([chr(int(decrypted_block[i][0]) + 65) for i in range(m)])
    return plain_text

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
plain_text = "HELLO"
cipher_text = hill_encrypt(plain_text, key_matrix)
decrypted_text = hill_decrypt(cipher_text, key_matrix)

print("Plaintext:", plain_text)
print("Ciphertext:", cipher_text)
print("Decrypted text:", decrypted_text)
