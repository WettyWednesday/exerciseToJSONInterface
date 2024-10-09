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

def submit(event=None):
    title = title_entry.get()
    description = description_entry.get()
    exercise_type = type_var.get()
    bodypart = bodypart_entry.get()
    equipment = equipment_var.get()
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

    save_exercise(exercise_data)
    messagebox.showinfo("Success", "Exercise added successfully!")
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    bodypart_entry.delete(0, tk.END)
    difficulty_var.set("Easy")
    type_var.set("Strength")
    equipment_var.set("Body Weight")

root = tk.Tk()
root.title("Exercise Tracker")
root.geometry("400x500")

label_font = ("Helvetica", 12, "bold")

tk.Label(root, text="Title: *", font=label_font).pack(pady=5)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

tk.Label(root, text="Description:", font=label_font).pack(pady=5)
description_entry = tk.Entry(root, width=50)
description_entry.pack(pady=5)

tk.Label(root, text="Type: *", font=label_font).pack(pady=5)
type_var = tk.StringVar(value="Strength")
type_dropdown = tk.OptionMenu(root, type_var, "Strength", "Endurance", "Cardio")
type_dropdown.pack(pady=5)

tk.Label(root, text="Body Part: *", font=label_font).pack(pady=5)
bodypart_entry = tk.Entry(root, width=50)
bodypart_entry.pack(pady=5)

tk.Label(root, text="Equipment: *", font=label_font).pack(pady=5)
equipment_var = tk.StringVar(value="Body Weight")
equipment_dropdown = tk.OptionMenu(root, equipment_var, "Body Weight", "Free Weights", "Machine")
equipment_dropdown.pack(pady=5)

tk.Label(root, text="Difficulty: *", font=label_font).pack(pady=5)
difficulty_var = tk.StringVar(value="Easy")
difficulty_dropdown = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
difficulty_dropdown.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

root.bind('<Return>', submit)

root.mainloop()
