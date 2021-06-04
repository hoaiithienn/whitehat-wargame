import sympy as sp
import hashlib

matrix = sp.Matrix([[1,2,3],[0,1,4],[5,6,0]])
cipher = 'UPCGIZGONLBHTBRJOLZEWKAY'

def convert_letters_to_numbers(letters):
	numbers = []
	for letter in letters:
		number = ord(letter.lower()) - 97
		numbers.append(number)
	return numbers

def convert_numbers_to_letters(numbers):
	letters = []
	for number in numbers:
		letter = chr(number + 97)
		letters.append(letter)
	return letters

def vectorize(numbers_array, sub_dim):
	if (len(numbers_array) % sub_dim != 0):
		raise ValueError("The length of cipher array must be divisible by the dimension of square key matrix!")

	number_vector = []
	for i in range(int(len(numbers_array) / sub_dim)):
		temp_vector = sp.Matrix(numbers_array[i*sub_dim : (i+1)*sub_dim])
		number_vector.append(temp_vector)

	return number_vector

def decrypt(message, key):
	message = convert_letters_to_numbers(message)
	message = vectorize(message, key.shape[0])
	result = []

	inverse_matrix = key.inv_mod(26)

	for i, cipher in enumerate(message):
		decipher = (inverse_matrix * cipher) % 26
		decipher_text = convert_numbers_to_letters(decipher)
		result += decipher_text

	result = ''.join(text for text in result)
	return result

def str2sha1(string):
	return hashlib.sha1(str(string).encode('utf-8')).hexdigest()

result = decrypt(cipher, matrix)
print('Original messages:  ', cipher.lower())
print('Decrypted messages: ', result)
print('Answer and its SHA1:')
print('\t ilovebronxvillenewyork')
print('\t -> WhiteHat{' + str2sha1('ilovebronxvillenewyork') + '}')
