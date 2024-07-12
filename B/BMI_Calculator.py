import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and configure the widgets
height_label = tk.Label(root, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
