def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    plaintext=plaintext+'.'*(len(key)-len(plaintext)%len(key))
    order = {
    num: int(val) for num, val in enumerate(key)
    }
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            if part[order[index]]==".":
                continue
            else:
                ciphertext+=part[order[index]]
    return ciphertext
key=input("Enter key : ")
plain_text=input("Enter the text to be encrypted : ")
print("cipher : ",encode(key,plain_text))