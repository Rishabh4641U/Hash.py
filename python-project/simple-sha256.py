# simple version for testing with dic-attack.py

import hashlib

password = input("Please enter your password: ")
hashed = hashlib.sha256(password.encode()).hexdigest()
print("=" * 40)
print("this is your hash 🔓🔓🔓👇")
print(f" your hash:  {hashed}")
