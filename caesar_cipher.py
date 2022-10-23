def encrypt(string,shift):
    cipher=""
    for i in string:
        if i == ' ':
            cipher+=i
        else:
            cipher+=chr((ord(i)-97+shift)%26+97)
    return cipher

text = input("Enter text to be encrypted : ")
s = int(input("Enter the shift value : "))
print(encrypt(text,s))
