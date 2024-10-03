import sys
from task_manager import TaskManager


def main():
    manager = TaskManager((1, 1, 1))

    while True:
        print()
        print("--- Task Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Sort Tasks")
        print("5. Set Weights")
        print("6. Display Weights")
        print("7. Exit")
        print()
        choice = input("Choose an option (1-6):\n")
        print()

        if choice == "1":
            try:
                title = str(input("Enter a title:\n"))

                urgency = float(input("Rate the urgency (0-1):\n"))

                if not (0 <= urgency <= 1):
                    raise ValueError

                importance = float(input("Rate the importance (0-1):\n"))

                if not (0 <= importance <= 1):
                    raise ValueError

                time_efficiency = float(input("Rate the time efficiency (0-1):\n"))

                if not (0 <= time_efficiency <= 1):
                    raise ValueError

                manager.add_task(
                    title, urgency - 0.5, importance - 0.5, time_efficiency - 0.5
                )

            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 1.")

        elif choice == "2":
            try:
                index = int(input("Enter the index of the task to remove:\n"))
                manager.remove_task(index)
            except ValueError:
                print("Invalid index. Please enter a valid integer.")

        elif choice == "3":
            print("\nTasks:")
            for index, task in enumerate(manager.tasks):
                print(
                    f"{index}. {task.title}: Category = '{task.category}', Priority = {task.priority(manager.weights)}, Urgency = {task.urgency + 0.5}, Importance = {task.importance + 0.5}, Time Efficiency = {task.time_efficiency + 0.5}"
                )

        elif choice == "4":
            manager.sort_tasks()
            print("\nTasks sorted!")

        elif choice == "5":
            try:
                urgency_weight = float(input("Input the urgency weight (0-1):\n"))

                if not (0 <= urgency_weight <= 1):
                    raise ValueError

                importance_weight = float(input("Input the importance weight (0-1):\n"))

                if not (0 <= importance_weight <= 1):
                    raise ValueError

                time_efficiency_weight = float(
                    input("Input the time efficiency weight (0-1):\n")
                )

                if not (0 <= time_efficiency_weight <= 1):
                    raise ValueError

                manager.weights = (
                    urgency_weight,
                    importance_weight,
                    time_efficiency_weight,
                )

            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 1.")

        elif choice == "6":
            urgency_weight, importance_weight, time_efficiency_weight = manager.weights
            print(
                f"\nWeights: Urgency Weight = {urgency_weight}, Importance Weight = {importance_weight}, Time Efficiency Weight = {time_efficiency_weight}"
            )

        elif choice == "7":
            print("Exiting Task Manager.")
            sys.exit()

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
