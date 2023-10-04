questions = [
    'Who led India to World Cup Victory in 2011?',
    'Who is the current prime minister of India?',
    'What is the capital of Maharashtra?',
    'Who is known as the god of cricket?',
    'When did India win its first World Cup in cricket?'
]
answers = [
    'MS Dhoni',
    'Narendra Modi',
    'Mumbai',
    'Sachin Tendulkar',
    '1983',
]
options = [
    ['MS Dhoni', 'Sunil Gavaskar', 'Virat Kohli', 'Rahul Dravid'],
    ['Manmohan Singh', 'Narendra Modi', 'Amit Shah', 'Sharad Pawar'],
    ['Pune', 'Nagpur', 'Mumbai', 'Aurangabad'],
    ['Sir Don Bradman', 'Ricky Ponting', 'Sir Vivian Richards', 'Sachin Tendulkar'],
    ['1983', '2011', '2007', '2013']
]

def play_game(username, questions, answers, options):
    print("Hello", username, "to the KBC Game!")
    score = 0
    for i in range(len(questions)):
        current_question = questions[i]
        correct_answer = answers[i]
        current_questions_options = options[i]
        print("Question :", current_question)
        for index, each_option in enumerate(current_questions_options):
            print(index+1, ') ', each_option, sep='')
        user_answer_index = int(input("Enter your choice (1,2,3 or 4) :"))
        user_answer = current_questions_options[user_answer_index - 1]
        if user_answer == correct_answer:
            print("Correct answer") 
            score = score + 100
        else:
            print("Wrong answer")
            break
    print("Your final score is :", score)
    return username, score
    pass
def view_scores(names_and_scores):
    for name, score in names_and_scores.items():
        print(name, "has scored", score)
    pass

def KBC(questions, answers, options):
    names_and_scores = {}
    while True:
        print("Welcome to the KBC Game!")
        print("1) Play Game\n2) View Scores\n3) Exit")
        choice = int(input("Please Enter Your Choice :"))
        if choice == 1:
            username = input("Please Enter Your Name :")
            username, score = play_game(username, questions, answers, options)
            names_and_scores[username] = score
        elif choice == 2:
            view_scores(names_and_scores)
        elif choice == 3:
            break
        else:
            print("Your choice is invalid!")
KBC(questions, answers, options,)      
