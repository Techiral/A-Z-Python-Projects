import settings

class QuizGame:
    def __init__(self) -> None:
        self. setting = settings.Settings()
        self.questions = self.setting.questions

    def prompt_user(self) -> None:
        print('\n'+'-'*60)
        print(" "*15+'WELCOME TO QUIZ GAME' + "\n" + '-' * 60)
        print("\n"+"Total of 10 questions 10 points each!!") 

    def start_game(self) -> None:
        game_points = 0
        for item in self.questions:
            print(item['question'])
            print("A. " + item['A'])
            print("B. " + item['B'])
            print("C. " + item['C'])
            print("D. " + item['D'])
            print('\n')
            answer = (input("Enter the correct option(A/B/C/D): ")).upper()
            if answer == item['correct']:
                print("-"*60+'\n CORRECT ANSWER \n' + '-' * 60)
                game_points += 10
                print(" "*15 +"GAME POINTS:" + str(game_points) + "\n" + '-' * 60)
            else:
                print("-"*60+'\n WRONG ANSWER \n'+'-'*60)
                print(" "*15 +"GAME POINTS:" + str(game_points) + "\n" + '-' * 60)


    def run_game(self) -> None:
        self.prompt_user() # function call
        is_start = input("\n DO you want to start the game (y for yes/ anu key for no): ")
        if is_start == 'y' or is_start == 'Y':
            self. start_game() #function call

if __name__ == '__main__':
   g = QuizGame()
   g.run_game()

