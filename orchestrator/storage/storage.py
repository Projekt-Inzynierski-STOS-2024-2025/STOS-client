# Module responsible for storing data about tasks. For now a simple dictionary.

from abc import ABC, abstractmethod
from typing import override

from orchestrator.types import Task

class IStorage(ABC):

    @abstractmethod
    def put(self, task: Task) -> None:
        pass

    @abstractmethod
    def get(self, id: str) -> Task:
        pass

    @abstractmethod
    def has_task(self, id: str) -> bool:
        pass

    @abstractmethod
    def delete_task(self, id: str) -> None:
        pass


class LocalStorage(IStorage):

    __storage: dict[str, Task] = {}

    @override
    def put(self, task: Task) -> None:
        self.__storage[task["id"]] = task

    @override
    def get(self, id: str) -> Task:
        return self.__storage.get(id) or {"":""}

    @override
    def has_task(self, id: str) -> bool:
        return self.__storage.get(id) is not None

    @override
    def delete_task(self, id: str) -> None:
        _ = self.__storage.pop(id)

        
        
