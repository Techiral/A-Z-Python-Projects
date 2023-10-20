import random

def choose_random_word():
    words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
    return random.choice(words)

def shuffle_word(word):
    shuffled = list(word)
    random.shuffle(shuffled)
    return ''.join(shuffled)

def play_word_jumble():
    original_word = choose_random_word()
    jumbled_word = shuffle_word(original_word)
    print("Welcome to Word Jumble!")
    print(f"Unscramble the letters to make a word: {jumbled_word}")
    
    attempts = 3

    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        if guess == original_word:
            print("Congratulations! You guessed the correct word!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess. You have {attempts} attempts left.")
            else:
                print("Sorry, you're out of attempts!")
                print(f"The correct word was: {original_word}")

if __name__ == "__main__":
    play_word_jumble()
