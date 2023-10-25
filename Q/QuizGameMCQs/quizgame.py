import random

# Define the list of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "correct_answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
        "correct_answer": "C",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Lion"],
        "correct_answer": "B",
    },
]

# Shuffle the order of questions
random.shuffle(questions)

# Initialize the score
score = 0

# Function to display a question and options, and get the user's answer
def display_question(question_obj):
    print(question_obj["question"])
    for option in question_obj["options"]:
        print(option)
    user_answer = input("Enter the letter corresponding to your answer (A, B, C, or D): ").upper()
    return user_answer

# Play the quiz
for question in questions:
    user_answer = display_question(question)
    if user_answer == question["correct_answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer is {question['correct_answer']}.\n")

# Display the final score
print(f"You scored {score}/{len(questions)}")

# Determine the result
if score == len(questions):
    print("Congratulations! You got all the questions right.")
elif score >= len(questions) // 2:
    print("Good job! You got more than half of the questions right.")
else:
    print("Keep practicing. You can do better next time!")
