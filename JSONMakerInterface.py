import tkinter as tk
from tkinter import messagebox
import json
import os

json_file = "exercises.json"

def load_data():
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            return json.load(file)
    return []

def save_exercise(data):
    exercises = load_data()

    exercises.append(data)

    with open(json_file, "w") as file:
        json.dump(exercises, file, indent=4)

def submit():
    title = title_entry.get();
    description = description_entry.get()
    exercise_type = type_var.get()
    bodypart = bodypart_entry.get()
    equipment = equipment_entry.get()
    difficulty = difficulty_var.get()

    if not title or not exercise_type or not bodypart or not equipment or not difficulty:
        messagebox.showwarning("Missing Fields", "Please fill in all required fields!")
        return

    exercise_data = {
        "title": title,
        "description": description,
        "type": exercise_type,
        "bodypart": bodypart,
        "equipment": equipment,
        "difficulty": difficulty
    }

    # Save the exercise to the JSON file
    save_exercise(exercise_data)

    # Show success message
    messagebox.showinfo("Success", "Exercise added successfully!")

    # Clear the form fields
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    bodypart_entry.delete(0, tk.END)
    equipment_entry.delete(0, tk.END)
    difficulty_var.set("Easy")
    type_var.set("Strength")

# GUI Setup
root = tk.Tk()
root.title("Exercise Tracker")
root.geometry("400x400")

# Title input
tk.Label(root, text="Title: *").pack(pady=5)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

# Description input
tk.Label(root, text="Description:").pack(pady=5)
description_entry = tk.Entry(root, width=50)
description_entry.pack(pady=5)

# Type dropdown
tk.Label(root, text="Type: *").pack(pady=5)
type_var = tk.StringVar(value="Strength")
type_dropdown = tk.OptionMenu(root, type_var, "Strength", "Endurance", "Cardio")
type_dropdown.pack(pady=5)

# Body part input
tk.Label(root, text="Body Part: *").pack(pady=5)
bodypart_entry = tk.Entry(root, width=50)
bodypart_entry.pack(pady=5)

# Equipment input
tk.Label(root, text="Equipment: *").pack(pady=5)
equipment_entry = tk.Entry(root, width=50)
equipment_entry.pack(pady=5)

# Difficulty dropdown
tk.Label(root, text="Difficulty: *").pack(pady=5)
difficulty_var = tk.StringVar(value="Easy")
difficulty_dropdown = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
difficulty_dropdown.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()