MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(text):
    encrypted_text = ''
    for i in text:
        if i == ' ':
            encrypted_text = encrypted_text + "    "
        else:
            encrypted_text  = encrypted_text + MORSE_CODE_DICT[i.upper()] + " "
    return encrypted_text


def decrypt(message):
    message += ' '  
    decipher = ''
    citext = ''
    i = 0  
    
    for letter in message:
        if letter != ' ':  
            i = 0
            citext += letter
        else:  
            i += 1
            if citext:  
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = '' 
            if i == 4:
                decipher += ' '

    return decipher

if __name__ == "__main__":
    print("Do you want to Encrypt or Decrypt?\n")
    print("1. Encrypt")
    print("2. Decrypt")
    opt = int(input("Choose your option (1 or 2): "))
    if opt == 1:
        text = input("Enter the text to Encrypt: ")
        print("Encrypted Text =", encrypt(text))
    elif opt == 2:
        text = input("Enter the text to Decrypt: ")
        print("Decrypted Text =", decrypt(text))


