# Module responsible for task management and docker container instances orchestration

from abc import ABC, abstractmethod
from typing import override

from orchestrator.storage.storage import IStorage
from orchestrator.types import Task, TaskHandler

class IOrchestrator(ABC):

    @abstractmethod
    def add_task(self, task: Task):
        pass

    @abstractmethod
    def register_on_task_completion(self, handler: TaskHandler):
        pass


class Orchestrator(IOrchestrator):

    __task_completion_handlers: list[TaskHandler] = []
    __storage: IStorage

    def __init__(self, storage: IStorage) -> None:
        self.__storage = storage

    @override
    def add_task(self, task: Task):
        if not self.__storage.has_task(task["id"]):
            self.__storage.put(task)
            self.__handle_new_task(task)

    @override
    def register_on_task_completion(self, handler: TaskHandler):
        self.__task_completion_handlers.append(handler)

    def __notify_task_completion(self, task: Task):
        for handler in self.__task_completion_handlers:
            handler(task)

    def __handle_new_task(self, task: Task):
        # TODO -actually do some container management. For now, just complete it
        self.__notify_task_completion(task)

