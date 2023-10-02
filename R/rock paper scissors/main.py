import random

banner = """
█▀█ █▀█ █▀▀ █▄▀ ░   █▀█ ▄▀█ █▀█ █▀▀ █▀█ ░   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
█▀▄ █▄█ █▄▄ █░█ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄ █   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
"""

def game():
    while True:
        print("\n1. Rock 🪨\n2. Paper 📜\n3. Scissors ✂️")
        user_choice = int(input("Enter your choice: "))
        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        computer_choice = random.randint(1, 3)

        print("Computer chose: ", choices[computer_choice])

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            print("Congratulations! You win! 🎉")
        else:
            print("Computer wins! Better luck next time! 🥹")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing! 👋")
            exit()
        else:
            game()

if __name__ == "__main__":
    print(banner)
    game()