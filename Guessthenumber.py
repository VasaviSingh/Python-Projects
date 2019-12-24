#This is a Guess the number game
import random

guessestaken=1
name=input("Enter Your name ") #inputsyourname
print("Hello " + name + " Welcome to GUESS THE NUMBER GAME ")

n=random.randint(1,99) #generates a random number between 1 and 99

while(guessestaken<5):    
      guess=int(input("Enter any number between 1 and 99 ")) #takes a number from user
      guessestaken+=1      
      if guess<n:
        print("Your guess is low")
      
      elif guess>n:
        print("Your guess is high")
        
      else:
        break;
if(guess==n):
    print("You did a great job")
else:
    print("You failed "+name)
