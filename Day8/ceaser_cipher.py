import os
os.system("cls")


print(
'''       
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
'''
)


alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]


def encode(text, shift):
    encrypted = ''
    for i in text:
        if i in alphabet:
            shifted_num = (alphabet.index(i) + shift) % len(alphabet)
            encrypted += alphabet[shifted_num]
        else:
            encrypted += i
    print(f"Here is the encoded text: {encrypted}")


def decode(text, shift):
    decrypted = ''
    for i in text:
        if i in alphabet:
            shifted_num = (abs(alphabet.index(i) - shift)) % 26
            decrypted = decrypted + alphabet[shifted_num] 
        else:
            decrypted += i
    print(f"Here is the decoded text: {decrypted}")


run = 'yes'
while run == 'yes':
    choice = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if choice == 'encode':
        msg = input("Type you message: \n").lower()
        num = int(input("Type the shift number: \n"))
        encode(text = msg, shift = num)
    elif choice == 'decode':
        msg = input("Type you message: \n").lower()
        num = int(input("Type the shift number: \n"))
        decode(text = msg, shift = num)
    
    run = input("Type 'yes' if you want to go again. Otherwise type 'no'.")


    
