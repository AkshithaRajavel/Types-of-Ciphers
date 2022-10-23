def encrypt(plaintext,substitution):
    ciphertext=''
    for i in plaintext:
        if i==" ":
            ciphertext+=i
        elif i.isupper():
            ciphertext+=substitution[ord(i)-65].toupper()
        else:
            ciphertext+=substitution[ord(i)-97]
    return ciphertext

subs_alph = "qwertyuiopasdfghjklzxcvbnm"
plain_text = input("Enter the plain text to be encrypted : ")
print("cipher text : ",encrypt(plain_text,subs_alph))
