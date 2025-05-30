import tkinter as tk
from tkinter import messagebox
import os

# File to save tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append((task, status == "1"))
    return tasks

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task, completed in task_list:
            file.write(f"{task}|{'1' if completed else '0'}\n")

# Add a new task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.append((task, False))
        update_listbox()
        save_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

# Delete selected task
def delete_task():
    try:
        index = task_listbox.curselection()[0]
        del task_list[index]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark task as completed/incomplete
def toggle_complete():
    try:
        index = task_listbox.curselection()[0]
        task, completed = task_list[index]
        task_list[index] = (task, not completed)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done/undone.")

# Update listbox with numbered tasks
def update_listbox():
    task_listbox.delete(0, tk.END)
    for i, (task, completed) in enumerate(task_list, start=1):
        display = f"{i}. [✔] {task}" if completed else f"{i}. [ ] {task}"
        task_listbox.insert(tk.END, display)

# Main GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

task_list = load_tasks()

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark Done/Undone", width=15, command=toggle_complete)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

update_listbox()
root.mainloop()
