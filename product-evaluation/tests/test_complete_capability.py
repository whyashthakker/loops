import pytest

from src.task_manager import TaskManager


def test_complete_task_marks_task_done_and_returns_it():
    manager = TaskManager()
    manager.create_task("Review PR")

    result = manager.complete_task(1)

    assert result == {"id": 1, "title": "Review PR", "done": True}
    assert manager.list_tasks()[0]["done"] is True


def test_complete_task_rejects_unknown_id():
    manager = TaskManager()
    manager.create_task("Exists")

    with pytest.raises(ValueError, match="not found"):
        manager.complete_task(999)
