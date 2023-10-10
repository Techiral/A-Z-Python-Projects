import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

def display_menu():
    print("O - Organizer Tool")
    print("==================")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Remove a task")
    print("4. Predict task priority")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def list_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
    else:
        print("No tasks found!")

def remove_task():
    list_tasks()
    choice = int(input("Enter the number of the task you want to remove: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 0 < choice <= len(tasks):
        del tasks[choice - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid choice!")

def train_model():
    df = pd.read_csv("dataset.csv")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["description"])
    priority_mapping = {"High": 2, "Medium": 1, "Low": 0}
    y = df["priority"].map(priority_mapping)
    model = LogisticRegression()
    model.fit(X, y)
    with open("model.pkl", "wb") as file:
        pickle.dump((model, vectorizer), file)

def predict_priority():
    task = input("Enter the task description: ")
    with open("model.pkl", "rb") as file:
        model, vectorizer = pickle.load(file)
    X = vectorizer.transform([task])
    prediction = model.predict(X)[0]
    priority_mapping = {2: "High", 1: "Medium", 0: "Low"}
    print(f"Predicted priority for the task: {priority_mapping[prediction]}")

def main():
    # Train the model once when the application starts
    train_model()

    while True:
        choice = display_menu()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            predict_priority()
        elif choice == "5":
            print("Thanks for using O - Organizer Tool!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
