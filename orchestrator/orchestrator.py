# Module responsible for task management and docker container instances orchestration

from abc import ABC, abstractmethod
from typing import override

from orchestrator.storage.storage import IStorage, LocalStorage
from orchestrator.strategy.strategy import DefaultOrchestratorStrategy, IOrchestratorStrategy
from orchestrator.types import Task, TaskHandler

# Interface used for communication with cache module
class IOrchestrator(ABC):

    # It should be called in a separate thread/coroutine - otherwise blocks
    @abstractmethod
    def add_task(self, task: Task):
        pass

    @abstractmethod
    def register_on_task_completion(self, handler: TaskHandler):
        pass

# Class used for management of containers according to the chosen strategy
class Orchestrator(IOrchestrator):

    __task_completion_handlers: list[TaskHandler] = []
    __storage: type[IStorage]
    __strategy: type[IOrchestratorStrategy]

    def __init__(self, storage: type[IStorage] = LocalStorage, strategy: type[IOrchestratorStrategy] = DefaultOrchestratorStrategy) -> None:
        self.__storage = storage
        self.__strategy = strategy

    @override
    def add_task(self, task: Task):
        if self.__strategy.can_add_task(self.__storage.get_all_tasks()):
            added_task = self.__storage.checked_put(task)
            if added_task:
                self.__handle_new_task(task)
            else: # Task already exists
                return
        else:
            # TODO - create buffer of to-be-added tasks, updated with task completion
            pass

    @override
    def register_on_task_completion(self, handler: TaskHandler):
        self.__task_completion_handlers.append(handler)

    def __notify_task_completion(self, task: Task):
        for handler in self.__task_completion_handlers:
            handler(task)

    def __handle_new_task(self, task: Task):
        # TODO -actually do some container management. For now, just complete it
        self.__notify_task_completion(task)

