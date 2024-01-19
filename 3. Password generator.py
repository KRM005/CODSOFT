import random
import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

all_characters = lowercase_letters + uppercase_letters + digits + special_characters

desired_length = int(input("Enter the desired length of the password: "))
password=""

for i in range(desired_length):
    temp=random.choice(all_characters)
    password+=temp

print("Generated Password:", password)
