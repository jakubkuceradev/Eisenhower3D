import sys
from cli.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, urgency, importance):
        new_task = Task(title, urgency, importance)
        self.tasks.append(new_task)
        print(f"\nAdded: {new_task}")

    def remove_task(self, index):
        print()
        try:
            removed_task = self.tasks.pop(index)
            print(f"Removed: {removed_task}")
        except IndexError:
            print("Error: Invalid task index.")

    def display_tasks(self):
        print()

        if not self.tasks:
            print("No tasks available.")
            return

        print("Tasks:")

        for index, task in enumerate(self.tasks):
            print(
                f"{index}. {task.title}: Urgency = {task.urgency}, Importance = {task.importance}"
            )


def main():
    manager = TaskManager()

    while True:
        print()
        print("--- Task Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        print()
        choice = input("Choose an option (1-4):\n")
        print()

        if choice == "1":
            try:
                title = str(input("Enter a title:\n"))

                urgency = float(input("Enter urgency (0-1):\n"))

                if not (0 <= urgency <= 1):
                    raise ValueError

                importance = float(input("Enter importance (0-1):\n"))

                if not (0 <= importance <= 1):
                    raise ValueError

                manager.add_task(title, urgency, importance)

            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 1.")

        elif choice == "2":
            try:
                index = int(input("Enter the index of the task to remove:\n"))
                manager.remove_task(index)
            except ValueError:
                print("Invalid index. Please enter a valid integer.")

        elif choice == "3":
            manager.display_tasks()

        elif choice == "4":
            print("Exiting Task Manager.")
            sys.exit()

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
