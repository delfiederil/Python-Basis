# Simple To-Do List CLI App

def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks yet!")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found. Add one first!")

# Example run
add_task("Learn Python functions")
add_task("Build mini project")
view_tasks()
