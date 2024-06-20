# Module responsible for storing data about tasks. For now a simple dictionary.

from abc import ABC, abstractmethod
from typing import override

from orchestrator.types import Task
from threading import Lock

class IStorage(ABC):

    # Add task to storage
    @staticmethod
    @abstractmethod
    def put(task: Task) -> None:
        pass

    # Get Task with provided id from storage
    @staticmethod
    @abstractmethod
    def get(id: str) -> Task:
        pass

    # Check whether task with provided id exists
    @staticmethod
    @abstractmethod
    def has_task(id: str) -> bool:
        pass

    # Remove task with provided id from storage
    @staticmethod
    @abstractmethod
    def delete_task(id: str) -> None:
        pass

    # List all tasks
    @staticmethod
    @abstractmethod
    def get_all_tasks() -> list[Task]:
        pass
    
    # Add task to storage if it does not exist
    @staticmethod
    @abstractmethod
    def checked_put(task: Task) -> bool:
        pass


class LocalStorage(IStorage):

    __storage: dict[str, Task] = {}
    __lock: Lock = Lock()

    @staticmethod
    @override
    def put(task: Task) -> None:
        with LocalStorage.__lock:
            LocalStorage.__storage[task["id"]] = task

    @staticmethod
    @override
    def get(id: str) -> Task:
        with LocalStorage.__lock:
            return LocalStorage.__storage.get(id) or {"":""}

    @staticmethod
    @override
    def has_task(id: str) -> bool:
        with LocalStorage.__lock:
            return LocalStorage.__storage.get(id) is not None

    @staticmethod
    @override
    def delete_task(id: str) -> None:
        with LocalStorage.__lock:
            _ = LocalStorage.__storage.pop(id)

    @staticmethod
    @override
    def get_all_tasks() -> list[Task]:
        with LocalStorage.__lock:
            return list(LocalStorage.__storage.values())

    @staticmethod
    @override
    def checked_put(task: Task) -> bool:
        with LocalStorage.__lock:
            if LocalStorage.__storage.get(task["id"]) is not None:
                return False
            else:
                LocalStorage.__storage[task["id"]] = task
                return True



        
        
