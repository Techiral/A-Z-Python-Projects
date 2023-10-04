import random

# List of words for the Hangman game
word_list = ["python", "programming", "hangman", "computer", "gaming"]

# Function to choose a random word from the word list
def choose_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word with blanks and guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main Hangman game loop
def hangman():
    word_to_guess = choose_word(word_list)
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts

    print("Welcome to Hangman!")
    
    while True:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Oops, that letter is not in the word.")
            attempts -= 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("\nGame over! The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
