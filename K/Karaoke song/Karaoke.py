import turtle
import random

# List of karaoke songs
karaoke_songs = [
    "Song 1",
    "Song 2",
    "Song 3",
    "Song 4",
    "Song 5",
]

# Function to display a recommendation
def display_recommendation(song):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write("Recommended Song:", align="center", font=("Arial", 20, "normal"))
    turtle.goto(0, 50)
    turtle.write(song, align="center", font=("Arial", 24, "bold"))

# Function to recommend a random song
def recommend_song(x, y):
    song = random.choice(karaoke_songs)
    display_recommendation(song)

# Set up the turtle window
def setup_window():
    turtle.setup(400, 400)
    turtle.bgcolor("lightblue")

# Create a clickable turtle shape
def create_clickable_turtle():
    clickable_turtle = turtle.Turtle()
    clickable_turtle.shape("circle")
    clickable_turtle.color("red")
    clickable_turtle.shapesize(2)
    clickable_turtle.penup()
    clickable_turtle.goto(0, 0)
    clickable_turtle.onclick(recommend_song)

# Main function
def main():
    setup_window()
    create_clickable_turtle()
    turtle.mainloop()

if __name__ == "__main__":
    main()
