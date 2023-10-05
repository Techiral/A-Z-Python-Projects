import random
import hangman_art
from word_list import words
choosen_word = random.choice(words)
word_length = len(choosen_word)
life = 6
game_end = False
temp = ''
display = []
for x in range(word_length): 
    display += "_" 
print("Welcome to hangman game")
print(f"total life = {life}")
print(hangman_art.logo)
print("word length = " + ' '.join(display))
while not game_end:
    guess = input("enter a letter ")
    life_loose = False
    x = 0
    if temp == guess:
        x = 1
        print(f"you already guessed {guess} letter")
    temp = guess
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display [position] = letter
    if guess in choosen_word:
        print("You choosed a correct letter :) ")
    if x == 0:
        if guess not in choosen_word:
            life_loose = True
    if life_loose:
        print(f"You guessed a wrong letter {guess}, You Loose a Life")
        life -= 1
        print(f"remaining life = {life}")
        print(hangman_art.stages[life])
        if life == 0:
            game_end = True
            print("Game Over :( ")
    print(' '.join(display))
    if "_" not in display:
        print("You win :) ")
        game_end = True
    