"""
Day 2/75
Strong_Password_Generator

"""

import random
import string

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)
    
print("Generated Password: ", password)