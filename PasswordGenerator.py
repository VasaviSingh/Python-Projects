#This is a program for generating passwords of 8 letters
import random
import string

def password():
    randomset=string.ascii_letters+string.digits+string.punctuation
    pasword=random.choice(string.ascii_lowercase)
    pasword+=random.choice(string.ascii_uppercase)
    pasword+=random.choice(string.digits)
    pasword+=random.choice(string.punctuation)
    
    for i in range(4):
        pasword+=random.choice(randomset)
    
    passwordlist=list(pasword)
    random.SystemRandom().shuffle(passwordlist)
    pasword=' '.join(passwordlist)
    return pasword

print("First password generated is: "+password())
print("Second password generated is: "+password())
    
    