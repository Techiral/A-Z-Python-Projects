import random
num = random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses=[0]


while True:
    guess=int(input("Guess the Num"))
    guesses.append(guess)
    if guess==num:
        print('Congratulation,correct guess')
        break
    elif 1>guess or guess>100:
        print('Guess an integer between 1 and 100')
    elif guesses[-2]:
        if (num-guess)<(num-guesses[-2]):
            print('warmer')
        else:
            print('colder')
    elif (num-10)<=guess<=(num+10):
        print('Warm')
    else:
        print('Cold')


print('Number of guesses were {g}'.format(g=len(guesses)))