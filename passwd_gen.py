import random

def password_generator(length=16):
    
    #characters that will be in the password
    chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ0123456789*#%'

    password=''
    i=0

    while i < length:
        password += random.choice(chars)
        i += 1
    
    return password

print(password_generator(10))# Generate a 10 characters long password
