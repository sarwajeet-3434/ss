def generate_key_square(key):
    key = key.upper().replace(" ", "")
    key_square = []
    seen = set()
    for char in key:
        if char not in seen and char != 'J':  # Remove 'J' for simplicity
            seen.add(char)
            key_square.append(char)
    for char in range(65, 91):  # A to Z (ASCII range)
        char = chr(char)
        if char not in seen and char != 'J':  # Skip 'J'
            key_square.append(char)
    return key_square

def preprocess_text(text):
    text = text.upper().replace(" ", "").replace("J", "I")  # Replace 'J' with 'I'
    processed_text = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:  # If the same character appears twice
            processed_text.append(text[i])
            processed_text.append('X')  # Insert 'X' to separate repeated characters
            i += 1
        else:
            processed_text.append(text[i:i + 2])  # Create digraphs
            i += 2
    # Handle the case of odd length plaintext by appending 'X' to the last character
    if len(processed_text[-1]) == 1:
        processed_text[-1] += 'X'
    return ["".join(processed_text[i:i + 2]) for i in range(0, len(processed_text), 2)]

def find_position(char, key_square):
    index = key_square.index(char)
    return divmod(index, 5)

def playfair_encrypt(plain_text, key):
    key_square = generate_key_square(key)
    processed_text = preprocess_text(plain_text)
    cipher_text = ""
    for digraph in processed_text:
        row1, col1 = find_position(digraph[0], key_square)
        row2, col2 = find_position(digraph[1], key_square)
        if row1 == row2:  # Same row
            cipher_text += key_square[row1 * 5 + (col1 + 1) % 5]
            cipher_text += key_square[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:  # Same column
            cipher_text += key_square[((row1 + 1) % 5) * 5 + col1]
            cipher_text += key_square[((row2 + 1) % 5) * 5 + col2]
        else:  # Rectangle
            cipher_text += key_square[row1 * 5 + col2]
            cipher_text += key_square[row2 * 5 + col1]
    return cipher_text

def playfair_decrypt(cipher_text, key):
    key_square = generate_key_square(key)
    processed_text = [cipher_text[i:i + 2] for i in range(0, len(cipher_text), 2)]
    plain_text = ""
    for digraph in processed_text:
        row1, col1 = find_position(digraph[0], key_square)
        row2, col2 = find_position(digraph[1], key_square)
        if row1 == row2:  # Same row
            plain_text += key_square[row1 * 5 + (col1 - 1) % 5]
            plain_text += key_square[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plain_text += key_square[((row1 - 1) % 5) * 5 + col1]
            plain_text += key_square[((row2 - 1) % 5) * 5 + col2]
        else:  # Rectangle
            plain_text += key_square[row1 * 5 + col2]
            plain_text += key_square[row2 * 5 + col1]
    return plain_text.rstrip('X')  # Remove padding 'X' only at the end

# Test the Playfair cipher
key = "KEYWORD"
plain_text = "HELLO"
cipher_text = playfair_encrypt(plain_text, key)
decrypted_text = playfair_decrypt(cipher_text, key)

# Corrected print statement (removed non-breaking space)
print("Plaintext:", plain_text)
print("Ciphertext:", cipher_text)
print("Decrypted text:", decrypted_text)
