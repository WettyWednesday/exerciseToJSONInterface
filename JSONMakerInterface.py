import tkinter as tk
from tkinter import messagebox
import json
import os
import csv

json_file = "exercises.json"
csv_file = "exercises.csv"

def load_data():
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            return json.load(file)
    return []

def save_exercise_json(data):
    exercises = load_data()
    exercises.append(data)
    with open(json_file, "w") as file:
        json.dump(exercises, file, indent=4)

def save_exercise_csv(data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Title", "Description", "Type", "Body Part", "Equipment", "Difficulty", "Time", "Time Unit"])
        writer.writerow([data['title'], data['description'], data['type'], data['bodypart'], data['equipment'], data['difficulty'], data['time'], data['time_unit']])

def convert_time():
    try:
        time_value = float(time_entry.get())
        if time_var.get() == "Seconds":
            time_entry.delete(0, tk.END)
            time_entry.insert(0, str(time_value / 60))
        elif time_var.get() == "Minutes":
            time_entry.delete(0, tk.END)
            time_entry.insert(0, str(time_value * 60))
    except ValueError:
        pass

def submit(event=None):
    title = title_entry.get()
    description = description_entry.get()
    exercise_type = type_var.get()
    bodypart = bodypart_entry.get()
    equipment = equipment_var.get()
    difficulty = difficulty_var.get()
    time_value = time_entry.get()
    time_unit = time_var.get()

    if not title or not exercise_type or not bodypart or not equipment or not difficulty or not time_value:
        messagebox.showwarning("Missing Fields", "Please fill in all required fields!")
        return

    exercise_data = {
        "title": title,
        "description": description,
        "type": exercise_type,
        "bodypart": bodypart,
        "equipment": equipment,
        "difficulty": difficulty,
        "time": time_value,
        "time_unit": time_unit
    }

    save_exercise_json(exercise_data)
    save_exercise_csv(exercise_data)
    
    messagebox.showinfo("Success", "Exercise added successfully!")
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    bodypart_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    difficulty_var.set("Easy")
    type_var.set("Strength")
    equipment_var.set("Body Weight")
    time_var.set("Seconds")  # Set to Seconds on submit reset

root = tk.Tk()
root.title("Exercise Tracker")
root.geometry("400x600")

window_width = 400
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2 - 100) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

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

tk.Label(root, text="Time: *", font=label_font).pack(pady=5)
time_frame = tk.Frame(root)
time_frame.pack(pady=5)
time_entry = tk.Entry(time_frame, width=20)
time_entry.pack(side=tk.LEFT, padx=5)
time_var = tk.StringVar(value="Seconds")  # Default to Seconds
time_dropdown = tk.OptionMenu(time_frame, time_var, "Seconds", "Minutes", command=lambda _: convert_time())
time_dropdown.pack(side=tk.LEFT)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

root.bind('<Return>', submit)

root.mainloop()
