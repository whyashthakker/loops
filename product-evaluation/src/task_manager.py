class TaskManager:
    """Minimal task manager — sample product for evaluation loops."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def create_task(self, title):
        task = {"id": self._next_id, "title": title, "done": False}
        self._next_id += 1
        self._tasks.append(task)
        return task

    def list_tasks(self, include_completed=True):
        if include_completed:
            return self._tasks
        return [t for t in self._tasks if not t["done"]]

    def complete_task(self, task_id):
        for task in self._tasks:
            if task["id"] == task_id:
                task["done"] = True
