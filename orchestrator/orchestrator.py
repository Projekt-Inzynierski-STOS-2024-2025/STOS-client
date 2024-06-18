# Module responsible for task management and docker container instances orchestration

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import override

type Task = dict[str, str]
type TaskCompletionHandler = Callable[[Task], None]

class IOrchestrator(ABC):

    @abstractmethod
    def add_task(self, task: Task):
        pass

    @abstractmethod
    def register_on_task_completion(self, handler: TaskCompletionHandler):
        pass


class Orchestrator(IOrchestrator):

    __task_completion_handlers: list[TaskCompletionHandler] = []

    @override
    def add_task(self, task: Task):
        pass

    @override
    def register_on_task_completion(self, handler: TaskCompletionHandler):
        self.__task_completion_handlers.append(handler)

    def _notify_task_completion(self, task: Task):
        for handler in self.__task_completion_handlers:
            handler(task)

