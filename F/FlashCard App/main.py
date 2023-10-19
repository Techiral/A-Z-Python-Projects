# Import required libraries
from tkinter import *
import pandas
import random

# Define background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize variables
current_card = {}
to_learn = {}

# Attempt to read the data from a CSV file
try:
    data = pandas.read_csv("data\words_to_learn.csv")
except FileNotFoundError:
    # If the file is not found, load data from a different CSV
    original_data = pandas.read_csv("F\FlashCard App\data\hindi_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # If data is successfully loaded, convert it to a list of dictionaries
    to_learn = data.to_dict(orient="records")

# Function to display the next flashcard
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# Function to flip the flashcard to reveal the English translation
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)

# Function to mark a card as known and remove it from the to-learn list
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("F/Flashcard App/data/words_to_learn.csv", index=False)
    next_card()

# Create the main window
window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create a canvas for displaying the flashcards
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="F\FlashCard App\images\card_front.png")
card_back_img = PhotoImage(file="F\FlashCard App\images\card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 68, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons for "unknown" and "known" flashcards
cross_img = PhotoImage(file="F\FlashCard App\images\wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="F/FlashCard App/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Display the first flashcard
next_card()

# Start the main GUI loop
window.mainloop()
