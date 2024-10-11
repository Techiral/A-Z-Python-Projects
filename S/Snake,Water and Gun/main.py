#rules
# s= snake, w=water, g=gun
# gun kills snake
# gun sinks in water
# snake drinks water

import random   #exteral module


def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':   # snake drinks water
            return False
        if you=='g':   # gun kills snake
            return True
    elif comp=='w':
        if you=='g':     # gun sinks in water
            return False
        if you=='s':       # snake drinks water
            return True
    elif comp=='g':
        if you=='s':    # gun kills snake
            return False
        if you=='w':     # gun sinks in water
            return True
        



print("Computer: Snake(s), Water(w) or Gun(g)?")
rand= random.randint(1,3)   #this function randomly chooses between numbers ranging from 1 to 3
if rand==1:
    comp='s'
elif rand==2:
    comp='w'
elif rand==3:
    comp='g'
print("Computer has Chosen")
you= input("Player: Snake(s), Water(w) or Gun(g)?\n")
result= game(comp,you)

if result==True:
    print("You Won!")
    print("Your Choice:",you)
    print("Computer's Choice:",comp)
elif result==False:
    print("You Lose!")
    print("Your Choice:",you)
    print("Computer's Choice:",comp)
elif result is None:
    print("Tie!")
    print("Your Choice:",you)
    print("Computer's Choice:",comp)