# A simplified version of the Wordament game
# the user has 6 attempts to guess the 5-letter word. 
# The program provides feedback on each guess, indicating which letters are correct and in the right position, 
# which letters are correct but in the wrong position, and which letters are not in the secret word. 
# If the user guesses the word correctly within the given number of attempts, they win the game. 
# Otherwise, they lose and the secret word is revealed.

import random

def is_word(user_word, secret_word):
    for i in range(5):
        if user_word[i] == secret_word[i]:
            print(user_word[i], end=' ')
        elif user_word[i] in secret_word:
            print(user_word[i].upper(), end=' ')
        else:
            print(user_word[i].lower(), end=' ')
    print()

    return user_word == secret_word

def play_wordament():
    words = ('apple', 'banana', 'cherry', 'grape', 'melon')
    random_word = random.choice(words)

    print("Welcome to Wordament!")
    print("Guess the 5-letter word.")

    attempts = 6
    while attempts > 0:
        user_word = input("Enter a 5-letter word: ")
        if len(user_word) != 5 or not user_word.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue

        if is_word(user_word, random_word):
            print("Congratulations! You guessed the word.")
            break
        else:
            attempts -= 1
            print("Wrong word. You have", attempts, "attempts left.")

    if attempts == 0:
        print("Game over. The word was", random_word)

play_wordament()
