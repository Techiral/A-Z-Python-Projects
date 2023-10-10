import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "Why did the bicycle fall over? Because it was two-tired!",
]

def tell_joke():
    # Randomly select a joke from the list
    joke = random.choice(jokes)
    return joke

while True:
    user_input = input("Tell me a joke (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if 'joke' in user_input.lower():
        print("Sure, here's a joke:")
        print(tell_joke())
    else:
        print("I can tell jokes. Just ask for one!")

