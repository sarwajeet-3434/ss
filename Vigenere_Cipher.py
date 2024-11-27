def generate_vigenere_table():
    table = []
    for i in range(26):
        table.append([chr((i + j) % 26 + 65) for j in range(26)])
    return table

def vigenere_encrypt(plain_text, key):
    table = generate_vigenere_table()
    plain_text = plain_text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    cipher_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            row = ord(char) - 65
            col = ord(key[key_index % len(key)]) - 65
            cipher_text += table[row][col]
            key_index += 1
        else:
            cipher_text += char
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    table = generate_vigenere_table()
    cipher_text = cipher_text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    plain_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            row = ord(key[key_index % len(key)]) - 65
            col = table[row].index(char)
            plain_text += chr(col + 65)
            key_index += 1
        else:
            plain_text += char
    return plain_text

key = "KEY"
plain_text = "HELLO VIGENERE"
cipher_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(cipher_text, key)

print("Plaintext:", plain_text)
print("Ciphertext:", cipher_text)
print("Decrypted text:", decrypted_text)
