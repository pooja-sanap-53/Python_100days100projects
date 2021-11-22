# Day 08
# Date: 22 Nov 2021
# Caesar Cipher Project


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
print('''
The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.  

It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. 
For example with a shift of 1, A would be replaced by B, B would become C, and so on. 

Feel free to give it a go and send encrpyted secret messages to your dear ones!!!''')

def caesar(start_text, shift_number, cipher_direction):
    end_text =""
    shift_number =  shift_number % 25
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "decode":
                new_positon = position -shift_number
            elif cipher_direction == "encode":
                new_positon = position + shift_number
            end_text += alphabet[new_positon]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(start_text = text, shift_number = shift, cipher_direction = direction)

    restart = input("Do you want to restart the CIPHER program?\nType 'yes' if you want to go again. Otherwise type 'no'").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")