# created by Abhishek_mishra209
import hashlib
import os

password = input("Please enter your password: ")

salt = os.urandom(16)
hashed = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode('utf-8'),
    salt,
    100000
)

print("this is your hash 🔓🔓🔓👇👇👇")
print(hashed.hex())