import random

def choose_word():
    # Define a list of words to jumble
    words = ["python", "guitar", "computer", "keyboard", "chocolate"]
    
    # Randomly select a word from the list
    return random.choice(words)

def jumble_word(word):
    # Create a jumbled version of the word
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def play_game():
    word_to_guess = choose_word()
    jumbled = jumble_word(word_to_guess)
    
    print("Welcome to the Word Jumble game!")
    print("Unscramble the word:", jumbled)
    
    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()
        if guess == word_to_guess:
            print("Congratulations! You unscrambled the word.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Try again. {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
            else:
                print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    play_game()
