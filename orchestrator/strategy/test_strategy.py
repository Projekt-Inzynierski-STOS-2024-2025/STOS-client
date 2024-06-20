from orchestrator.strategy.strategy import DefaultOrchestratorStrategy
from orchestrator.types import Task

def test_default_overflow():
    tasks: list[Task] = []
    for _ in range(10):
        assert DefaultOrchestratorStrategy.can_add_task(tasks)
        tasks.append({"id": "some id"})
    assert (not DefaultOrchestratorStrategy.can_add_task(tasks))
