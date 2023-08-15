def caeser_cipher(plaintext,key):
    ciphertext=""
    for char in plaintext:
        if char.isalpha():
            base =ord('A') if char.isupper() else ord('a')
            shifttext=chr((ord(char)-base + key)% 26+ base) 
            ciphertext+=shifttext
        else:
            ciphertext+=char
    return ciphertext

def caeser_decrypt(ciphertext,key):
    return caeser_cipher(ciphertext,-key)

plaintext ="hello"
key=8

encrypted_text= caeser_cipher(plaintext,key)
print("encrypr:",encrypted_text)

de= caeser_decrypt(encrypted_text,key)
print("decry:",de)