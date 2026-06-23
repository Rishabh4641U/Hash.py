import bcrypt

password = input("Enter your password please: ")

# hash the password
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(hashed)