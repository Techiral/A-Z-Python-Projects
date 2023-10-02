import random

def magic_8_ball():
    responses = ["Yes", "No", "Maybe", "Ask again later", "Outlook not so good"]
    
    while True:
        question = input("Ask the Magic 8-Ball a yes-or-no question (or type 'exit' to quit): ")
        
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = random.choice(responses)
        print(f"Magic 8-Ball says: {response}\n")

if __name__ == "__main__":
    print("Welcome to the Magic 8-Ball Fortune Teller!")
    magic_8_ball()
