class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTaskMaster - Your To-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task description: ")
            task_manager.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            task_manager.remove_task(task)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
