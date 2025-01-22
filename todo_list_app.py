import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Functions to handle tasks
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, completed = line.strip().rsplit(",", 1)
                tasks_listbox.insert(tk.END, task)
                if completed == "True":
                    tasks_listbox.itemconfig(tk.END, fg="gray")


def save_tasks():
    with open(TASK_FILE, "w") as file:
        for i in range(tasks_listbox.size()):
            task = tasks_listbox.get(i)
            is_completed = tasks_listbox.itemcget(i, "fg") == "gray"
            file.write(f"{task},{is_completed}\n")

def add_task():
    task = task_entry.get().strip()
    if not task:
        status_label.config(text="Error: Task cannot be empty", fg="red")
        return

    tasks_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks()
    status_label.config(text="Task added", fg="green")

def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        save_tasks()
        status_label.config(text="Task removed", fg="green")
    except IndexError:
        status_label.config(text="Error: No task selected", fg="red")

def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        current_color = tasks_listbox.itemcget(selected_task_index, "fg")
        new_color = "gray" if current_color != "gray" else "black"
        tasks_listbox.itemconfig(selected_task_index, fg=new_color)
        save_tasks()
        status_label.config(text="Task marked as completed", fg="green")
    except IndexError:
        status_label.config(text="Error: No task selected", fg="red")

def clear_all():
    tasks_listbox.delete(0, tk.END)
    save_tasks()
    status_label.config(text="All tasks cleared", fg="green")

# Create the main application window
root = tk.Tk()
root.title("Todo List Application")
root.geometry("400x400")

# Entry for new tasks
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Buttons for task operations
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.grid(row=0, column=2, padx=10, pady=10)

remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.grid(row=1, column=0, padx=10, pady=10)

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_completed_button.grid(row=1, column=1, padx=10, pady=10)

clear_all_button = tk.Button(root, text="Clear All", command=clear_all)
clear_all_button.grid(row=1, column=2, padx=10, pady=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
tasks_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.grid(row=3, column=0, columnspan=3, pady=10)

# Load tasks from file
load_tasks()

# Run the Tkinter event loop
root.mainloop()
