def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += 97
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
plain_text = input("Enter the plain text to be encrypted : ")
keyword = input("Enter the keyword : ")
key = generateKey(plain_text, keyword)
print("Ciphertext :", cipherText(plain_text,key))
