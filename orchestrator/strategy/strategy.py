from abc import ABC, abstractmethod
from typing import override
import os

from orchestrator.types import Task


class IOrchestratorStrategy(ABC):

    @staticmethod
    @abstractmethod
    def can_add_task(tasks: list[Task]) -> bool: 
        pass

    @staticmethod
    def check_tasks_health(tasks: list[Task]) -> list[bool]:
        health_list: list[bool] = []
        for task in tasks:
            health_list.append(IOrchestratorStrategy._check_task_health(task))
        return health_list

    @staticmethod
    @abstractmethod
    def _check_task_health(task: Task) -> bool:
        pass


# The simplest possible strategy with basic timeout and healthceck, with params being pulled from environment vars
class DefaultOrchestratorStrategy(IOrchestratorStrategy):

    # Default timeout in seconds, after which container are kill, defaults to 60 seconds
    TIMEOUT = os.environ.get("TASK_TIMEOUT", 60)

    # Maximum amount of tasks being processed simultaneausly, defaults to 10
    MAX_TASKS: int = int(os.environ.get("MAX_TASKS", 10))

    @staticmethod
    @override
    def can_add_task(tasks: list[Task]) -> bool:
        return (len(tasks) < DefaultOrchestratorStrategy.MAX_TASKS)

    @staticmethod
    @override
    def _check_task_health(task: Task) -> bool:
        # TODO - actually do healthchecks, for now we assume task is healthy
        return True

