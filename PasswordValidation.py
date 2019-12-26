# Python program to check validation of password 
# Module of regular expression is used with search() 
import re 
password = "Po2@3_S"
flag = 0
while True: 
	if (len(password)<8): #checks for length of the password
		flag = -1
		break
	elif not re.search("[a-z]", password): #condition becomes true if there are no lowercase letters
		flag = -1
		break
	elif not re.search("[A-Z]", password): #condition becomes true if there are no uppercase letters
		flag = -1
		break
	elif not re.search("[0-9]", password): #condition becomes true if there are no digits
		flag = -1
		break
	elif not re.search("[_@$]", password): #condition becomes true if following [_@$]are not present
		flag = -1
		break
	elif re.search("\s", password): #condition becomes true if there is any whitespace character  
		flag = -1
		break
	else: 
		flag = 0
		print("Valid Password") 
		break

if flag ==-1: 
	print("Not a Valid Password") 
