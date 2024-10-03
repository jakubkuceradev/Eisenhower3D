class Task:
    def __init__(self, title, urgency, importance):
        self.title = title
        self.urgency = urgency
        self.importance = importance

    def __repr__(self):
        return f"Task(title={self.title}, urgency={self.urgency}, importance={self.importance})"
