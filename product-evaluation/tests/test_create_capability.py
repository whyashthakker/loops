import pytest

from src.task_manager import TaskManager


def test_create_task_returns_new_task_with_id():
    manager = TaskManager()

    task = manager.create_task("Ship release")

    assert task == {"id": 1, "title": "Ship release", "done": False}


def test_create_task_rejects_empty_title():
    manager = TaskManager()

    with pytest.raises(ValueError, match="title"):
        manager.create_task("")


def test_create_task_rejects_whitespace_title():
    manager = TaskManager()

    with pytest.raises(ValueError, match="title"):
        manager.create_task("   ")
