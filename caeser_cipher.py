def caesar_cipher(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Enter the plain/cipher text: ")
s = int(input("If you want to encrypt the text, enter a positive Key value. \nIf you want to decrypt the text, enter a negative Key value: "))
print("Text: ", text)
print("Key: ", str(s))
print("Result: ", caesar_cipher(text, s))
