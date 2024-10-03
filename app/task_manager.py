class Task:
    def __init__(
        self, title: str, urgency: float, importance: float, time_efficiency: float
    ):
        self.title = title
        self.urgency = urgency
        self.importance = importance
        self.time_efficiency = time_efficiency

        if self.urgency >= 0:
            if self.importance >= 0:
                self.category = "Do Now"
            else:
                self.category = "Do Later"
        else:
            if self.importance >= 0:
                self.category = "Delegate"
            else:
                self.category = "Delete"

    def __repr__(self) -> str:
        return f"Task(title={self.title}, urgency={self.urgency}, importance={self.importance}, time_efficiency={self.time_efficiency})"

    def priority(self, weights: tuple[float, float, float]) -> float:
        urgency_weight, importance_weight, time_efficiency_weight = weights
        return (
            (self.urgency * urgency_weight)
            + (self.importance * importance_weight)
            + (self.time_efficiency * time_efficiency_weight)
        )

    def category(self, weights: tuple[float, float, float] = {0.5, 0.5, 0.5}):
        urgency_weight, importance_weight, time_efficiency_weight = weights

        if self.urgency >= 0:
            if self.importance >= 0:
                return "Do Now"
            else:
                return "Do Later"
        else:
            if self.importance >= 0:
                return "Delegate"
            else:
                return "Delete"


class TaskManager:
    def __init__(self, weights: tuple[float, float, float]):
        self.tasks: list[Task] = []
        self.weights = weights

    def add_task(
        self, title: str, urgency: float, importance: float, time_efficiency: float
    ):
        new_task = Task(title, urgency, importance, time_efficiency)
        self.tasks.append(new_task)

    def remove_task(self, index: int):
        self.tasks.pop(index)

    def sort_tasks(self):
        self.tasks.sort(key=lambda task: task.priority(self.weights), reverse=True)

    def __repr__(self) -> str:
        return f"TaskManager(tasks={self.tasks})"
