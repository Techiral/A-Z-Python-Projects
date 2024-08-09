import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import time
import pygame

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Quiz")
        self.root.geometry("800x500")
        style = ThemedStyle(root)
        style.set_theme("plastik")  # Apply the Plastik theme

        self.questions = [
    {
        "question": "What is the capital of France?",
        "options": ["New York", "London", "Paris", "Berlin"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Kangaroo"],
        "correct_answer": "Blue Whale",
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1912", "1920", "1935", "1943"],
        "correct_answer": "1912",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon Dioxide",
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Liver", "Lungs", "Skin", "Heart"],
        "correct_answer": "Skin",
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "South Korea", "Japan", "Thailand"],
        "correct_answer": "Japan",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "correct_answer": "Au",
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Leo Tolstoy"],
        "correct_answer": "William Shakespeare",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Saturn", "Jupiter"],
        "correct_answer": "Jupiter",
    },
]


        self.score = 0
        self.current_question = 0
        self.timer_label = None

        self.name_label = ttk.Label(root, text="Enter your name:")
        self.name_label.pack(pady=5)
        self.name_entry = ttk.Entry(root)
        self.name_entry.pack(pady=5)

        self.question_label = ttk.Label(root, text="", font=("Helvetica", 18), wraplength=600)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = ttk.Button(root, text="", style="TButton", command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.score_label = ttk.Label(root, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack(pady=20)

        # New features: High Scores and Sound Effects
        self.high_scores = {}  # Dictionary to store high scores

        # Initialize Pygame for sound
        pygame.mixer.init()

        # Load sound files for correct and incorrect answers
        self.correct_sound = pygame.mixer.Sound("correct.mp3")
        self.incorrect_sound = pygame.mixer.Sound("incorrect.mp3")

        self.load_question(0)

    def load_question(self, question_index):
        question_data = self.questions[question_index]
        self.question_label.config(text=question_data["question"])
        random.shuffle(question_data["options"])

        for i in range(4):
            self.option_buttons[i].config(text=question_data["options"][i])

        self.current_question = question_index

        if self.timer_label:
            self.timer_label.destroy()

        self.timer_label = ttk.Label(self.root, text="Time Left: 20", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)
        self.start_timer(20)

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        if question_data["options"][selected_option] == question_data["correct_answer"]:
            self.score += 1
            self.correct_sound.play()  # Play the correct answer sound
        else:
            self.incorrect_sound.play()  # Play the incorrect answer sound

        if self.current_question < len(self.questions) - 1:
            self.load_question(self.current_question + 1)
        else:
            user_name = self.name_entry.get()
            self.update_high_scores(user_name, self.score)  # Update high scores
            messagebox.showinfo("Quiz Completed", f"Congratulations, {user_name}! You scored {self.score} out of {len(self.questions)}.")
            self.root.quit()

        self.score_label.config(text=f"Score: {self.score}")

    def start_timer(self, seconds):
        if seconds == 0:
            question_data = self.questions[self.current_question]
            correct_index = question_data["options"].index(question_data["correct_answer"])
            self.show_correct_answer(correct_index)
        else:
            self.timer_label.config(text=f"Time Left: {seconds}")
            self.root.after(1000, self.start_timer, seconds - 1)

    def show_correct_answer(self, correct_index):
        for i, button in enumerate(self.option_buttons):
            if i == correct_index:
                button.configure(style="Correct.TButton")
            else:
                button.configure(state="disabled")

    # New feature: Update High Scores
    def update_high_scores(self, user_name, score):
        if user_name in self.high_scores:
            if score > self.high_scores[user_name]:
                self.high_scores[user_name] = score
        else:
            self.high_scores[user_name] = score

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
