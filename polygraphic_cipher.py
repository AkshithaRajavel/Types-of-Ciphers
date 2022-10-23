def getKeyMatrix(key):
	k = 0
	for i in range(n):
		for j in range(n):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1
def encrypt(messageVector):
	for i in range(n):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(n):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26
def HillCipher(message, key):
	getKeyMatrix(key)
	for i in range(n):
		messageVector[i][0] = ord(message[i]) % 65
	encrypt(messageVector)
	CipherText = []
	for i in range(n):
		CipherText.append(chr(cipherMatrix[i][0] + 65))
	print("Ciphertext: ", "".join(CipherText))
n = int(input("Enter length of plain text to be encrypted : "))
message = input(f"Enter the {n} letter word : ")
key = input(f"Enter the {n*n} letter key : ")
keyMatrix = [[0] * n for i in range(n)]
messageVector = [[0] for i in range(n)]
cipherMatrix = [[0] for i in range(n)]
HillCipher(message, key)
