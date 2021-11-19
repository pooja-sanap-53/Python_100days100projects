# Day 05
# Date: 19 Nov 2021
# Password Generator 

'''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

'''
import random

print("**********************Welcome to Password Generator**********************")
us_letters = int(input("How many letters would you like in your password?"))
us_symbols = int(input("How many symbols would you like?"))
us_numbers = int(input("how many numbers would you like?"))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


for i in letters :
    rand_let = random.choices(letters, k=us_letters)

for i in numbers :
    rand_num  = random.choices( numbers , k=us_numbers)

for i in symbols :
    rand_sym = random.choices(symbols, k=us_symbols)
    
raw_password = (rand_let + rand_sym + rand_num )

# Easy level - without randomization 
password_order = ""
for i in raw_password:
    password_order += i
print(f"Your password in unrandomized order is {password_order}")


# Hard level - with randomization 
random.shuffle(raw_password)

password = ""
for i in raw_password:
    password += i
print(f"Your password in randomized order is {password}")

