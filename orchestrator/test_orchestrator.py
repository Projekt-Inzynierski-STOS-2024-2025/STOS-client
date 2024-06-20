from orchestrator.orchestrator import Orchestrator
from orchestrator.types import Task
from orchestrator.storage.storage import LocalStorage

def test_add_task():
    o = Orchestrator()

    o.add_task({"id": "stuff", "foo": "bar"})
    assert(LocalStorage.has_task("stuff"))

    o.add_task({"id": "stuff", "foo": "zooom"})

    attr = LocalStorage.get("stuff")["foo"]
    
    assert(attr == "bar")

def test_add_notify():
    o = Orchestrator()

    id = ""
    def callback(task: Task) -> None:
        nonlocal id
        id = task["id"]

    o.register_on_task_completion(callback)
    o.add_task({"id": "test"})

    assert (id == "test")

def test_add_too_many():
    o = Orchestrator()

    for i in range(2000):
        o.add_task({"id": str(i)})

    assert len(LocalStorage.get_all_tasks()) == 10
