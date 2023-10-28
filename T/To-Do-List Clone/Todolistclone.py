import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Create and configure the Add and Delete buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
add_button.pack()
delete_button.pack()

# Create and configure the task listbox
task_listbox = tk.Listbox(root, selectbackground="yellow", selectmode=tk.SINGLE)
task_listbox.pack()

# Run the application
root.mainloop()
