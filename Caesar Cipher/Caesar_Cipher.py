import Caesar_Cipher_art

#TODO: Choice fuction defined
def choice(direction,):
    if "encode" == direction:
        encrypt(text,shift)
    elif "decode" == direction:
        decrypt(text,shift)
    else:
        print("Wrong Input")

#TODO: Encryption Function Defined
def decrypt(text,shift):
    original_message = ''
    for i in range(0,len(text)):
        if text[i] in Caesar_Cipher_art.alphabet:
            index = Caesar_Cipher_art.alphabet.index(text[i])
            negative_shift = (index - shift)
            if negative_shift<0:
                original_message += Caesar_Cipher_art.alphabet[(negative_shift+26)]
            else:
                original_message += Caesar_Cipher_art.alphabet[(negative_shift)]
        else:
            original_message += text[i]
    print(f"Original Message:{original_message}")

#TODO: Decryption Function Defined
def encrypt(text,shift):
    # print(f"The plain text message:{text}")
    cipher_txt = ''
    for i in range(0,len(text)):
       if text[i] in Caesar_Cipher_art.alphabet:
           index = Caesar_Cipher_art.alphabet.index(text[i])
           cipher_txt += Caesar_Cipher_art.alphabet[(index+shift)%26]
       else:
           cipher_txt+=text[i]
    print(f"Cipher_txt:{cipher_txt}")


#MAIN FUCTION
print(Caesar_Cipher_art.logo)
x=False
while not x:
    text = list(input("Text:").lower())
    shift = int(input("Type the shift number:"))
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    choice(direction)
    input1 = input("To continue,Type Y and N:")
    if input1=='Y':
        continue
    elif input1=='N':
        break

    else:
        print("Invalid")
print("Game Over!!")




