
import random

import string_utils

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""

for i in range(0 , nr_letters):

  rand_letter_posi = random.randint(0,27)

  password = password + letters[rand_letter_posi]

# print(password)

for i in range(0,nr_symbols):

  rand_sym_posi = random.randint(0,8)

  password = password+symbols[rand_sym_posi]

# print(password)

for i in range(0 , nr_numbers):

  rand_num_posi = random.randint(0, 9)

  password = password+ numbers[rand_num_posi]

print(f"Your password is: {password}")  

print(f"You can use shuffled password too! : {string_utils.shuffle(password)}")
