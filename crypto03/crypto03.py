import string
import hashlib

def str2sha1(string):
    return hashlib.sha1(str(string).encode('utf-8')).hexdigest()

def getSHA1answer(string):
    return 'WhiteHat{' + str2sha1(string) + '}'
# Read file
with open('cipher.txt') as f:
	message = f.read()
key = 'HASAGY'

# Create alphabet:
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

def decrypt(message, key):
    decrypted_message = []
    current_key_idx = 0

    for c in message:
        if c in alphabet_lower: 
            decrypted_text = chr(ord('a') + ((ord(c) - ord(key[current_key_idx].lower()) + 26) % 26))
            decrypted_message.append(decrypted_text)
            current_key_idx = (current_key_idx + 1) % len(key)
        elif c in alphabet_upper:
            decrypted_text = chr(ord('A') + ((ord(c) - ord(key[current_key_idx]) + 26) % 26))
            decrypted_message.append(decrypted_text)
            current_key_idx = (current_key_idx + 1) % len(key)  
        else:
            decrypted_message.append(c)

    decrypted_message = ''.join(letter for letter in decrypted_message)

    return decrypted_message


print('Key decoding: Horse = H, Elephant = E, Yak = Y, Alligator = A, Seahorse = S, Goat = G')
print('So the meaning of key.png is: KEY = \'HASAGY\'')
print('Decrypted message:')
print(decrypt(message, key))
print('Flag is b3st_T4l0n_blu3_t3am')
print('Its SHA1:', str2sha1('b3st_T4l0n_blu3_t3am'))
print('Final answer:', getSHA1answer('b3st_T4l0n_blu3_t3am'))
