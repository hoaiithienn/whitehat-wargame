import string
import hashlib

def str2sha1(string):
	return hashlib.sha1(str(string).encode('utf-8')).hexdigest()

def getSHA1answer(string):
	return 'WhiteHat{' + str2sha1(string) + '}'

# Read file
with open('storyofryze.txt') as f:
	message = f.read()

# Create alphabet:
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

# Ceasar decoder:
def decode(message, shift_number):
	shifted_message = []
	for c in message:
		if c in alphabet_lower:
			shifted_message.append(chr(97 + ((ord(c) + shift_number - 97) % 26)))
		elif c in alphabet_upper:
			shifted_message.append(chr(65 + ((ord(c) + shift_number - 65) % 26)))
		else:
			shifted_message.append(c)
	shifted_message = ''.join(letter for letter in shifted_message)
	return shifted_message

# Brute force decoder:
for shift_number in range(1,27):
	shifted_message = decode(message, shift_number)
	print(f'---------------------------- shift_number = {shift_number} ----------------------------------------------')
	print(shifted_message)

# Answer:
print('--------------------------------------------------------------------------------')
print('After examining the results, shift_number = 5 makes sense!')
print('Flag is n0_d1e_c4n_w1n')
print('Its SHA1:', str2sha1('n0_d1e_c4n_w1n'))
print('Final answer:', getSHA1answer('n0_d1e_c4n_w1n'))
