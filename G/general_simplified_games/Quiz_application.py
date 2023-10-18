class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for question, options, answer in self.questions:
            print(question)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            user_answer = int(input("Your choice (1/2/3/4): "))
            if options[user_answer-1] == answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Correct answer is: {answer}\n")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
        ("Which is the smallest prime number?", ["0", "1", "2", "3"], "2"),
        ("What language is this code written in?", ["Java", "Python", "C++", "JavaScript"], "Python")
    ]
    
    game = Quiz(questions)
    game.play()
