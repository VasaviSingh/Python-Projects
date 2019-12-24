import random
import time
def dice():
    player=random.randint(1,6)
    print("You rolled: "+str(player))

    comp=random.randint(1,6)
    time.sleep(3)
    print("Computer rolled: "+str(comp))
    
    if(player>comp):
        print("You win")
    else:
        print("You lose")
        
        
    print("To continue press y else press n")
    choice=input()

    if(choice=='y' or choice=='Y'):
        dice()
    else:
        exit()

print("Press S to roll your die.")
roll = input()
if roll=='S' or roll=='s':
   dice()
else:
    exit()
