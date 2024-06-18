# Module responsible for task management and docker container instances orchestration

from abc import ABC, abstractmethod
from collections.abc import Callable

class IOrchestrator(ABC):

    @abstractmethod
    def add_task(self, task: dict[str, str]):
        pass

    @abstractmethod
    def register_on_task_completion(self, handler: Callable[[dict[str, str]], None]):
        pass



class Orchestrator:
    pass
