from src.task_manager import TaskManager


def test_list_tasks_returns_snapshot_not_internal_reference():
    manager = TaskManager()
    manager.create_task("Write docs")

    tasks = manager.list_tasks()
    tasks.clear()

    assert manager.list_tasks() == [{"id": 1, "title": "Write docs", "done": False}]


def test_list_tasks_can_exclude_completed():
    manager = TaskManager()
    manager.create_task("Open item")
    manager.create_task("Done item")
    manager.complete_task(2)

    assert manager.list_tasks(include_completed=False) == [
        {"id": 1, "title": "Open item", "done": False}
    ]
