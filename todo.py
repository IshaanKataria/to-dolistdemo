import json

# Load tasks from a file (or start empty)
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add task  2. View tasks  3. Complete task  4. Quit")
        choice = input("Choose: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
        elif choice == "2":
            for i, t in enumerate(tasks):
                status = "✓" if t["done"] else " "
                print(f"{i+1}. [{status}] {t['task']}")
        elif choice == "3":
            num = int(input("Task number: ")) - 1
            tasks[num]["done"] = True
            save_tasks(tasks)
        elif choice == "4":
            break

main()