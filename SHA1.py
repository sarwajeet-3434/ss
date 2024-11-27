import hashlib


def calculate_sha1(input_string):
    sha1_hash = hashlib.sha1() 
    sha1_hash.update(input_string.encode('utf-8'))  
    return sha1_hash.hexdigest()  

if __name__ == '__main__':
    text = "Hello, World!" 
    sha1_result = calculate_sha1(text) 
    print(f'SHA-1 hash of "{text}": {sha1_result}')  
