from datetime import datetime
import pickle

class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.description} - Priority: {self.priority}, Due: {self.due_date}, Status: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, priority, due_date):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]
        self.save_tasks()

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                break
        self.save_tasks()

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def save_tasks(self):
        with open('tasks.pkl', 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open('tasks.pkl', 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []

def main():
    manager = TaskManager()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            manager.add_task(description, priority, due_date)
        elif choice == '2':
            description = input("Enter task description to remove: ")
            manager.remove_task(description)
        elif choice == '3':
            description = input("Enter task description to mark as completed: ")
            manager.mark_task_completed(description)
        elif choice == '4':
            manager.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
