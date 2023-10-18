import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100, inclusive. Can you guess it?")

    while guess != random_number:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            
            # Increment the attempt counter
            attempts += 1

            # Check if the guess is correct
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        number_guessing_game()

if __name__ == "__main__":
    number_guessing_game()
