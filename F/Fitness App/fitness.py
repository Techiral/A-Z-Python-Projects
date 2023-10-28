class Workout:
    def __init__(self, exercise, duration, calories_burned):
        self.exercise = exercise
        self.duration = duration
        self.calories_burned = calories_burned

class FitnessApp:
    def __init__(self):
        self.workouts = []

    def add_workout(self, exercise, duration, calories_burned):
        workout = Workout(exercise, duration, calories_burned)
        self.workouts.append(workout)

    def show_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
            return

        total_calories = sum(workout.calories_burned for workout in self.workouts)
        total_duration = sum(workout.duration for workout in self.workouts)

        print("Workout History:")
        for i, workout in enumerate(self.workouts, 1):
            print(f"Workout {i}: {workout.exercise} ({workout.duration} minutes, {workout.calories_burned} calories burned)")

        print(f"Total workouts: {len(self.workouts)}")
        print(f"Total duration: {total_duration} minutes")
        print(f"Total calories burned: {total_calories} calories")

def main():
    fitness_app = FitnessApp()

    while True:
        print("\nFitness App Menu:")
        print("1. Add Workout")
        print("2. Show Workouts")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            exercise = input("Enter the exercise: ")
            duration = float(input("Enter the duration (minutes): "))
            calories_burned = float(input("Enter calories burned: "))
            fitness_app.add_workout(exercise, duration, calories_burned)
            print("Workout added successfully!")

        elif choice == '2':
            fitness_app.show_workouts()

        elif choice == '3':
            print("Exiting Fitness App.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
