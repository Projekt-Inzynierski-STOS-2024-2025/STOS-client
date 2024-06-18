from orchestrator.orchestrator import Orchestrator
from orchestrator.types import Task
from orchestrator.storage.storage import LocalStorage

def test_add_task():
    s = LocalStorage()
    o = Orchestrator(s)

    o.add_task({"id": "stuff", "foo": "bar"})
    assert(s.has_task("stuff"))

    o.add_task({"id": "stuff", "foo": "zooom"})

    attr = s.get("stuff")["foo"]
    
    assert(attr == "bar")

def test_add_notify():
    s = LocalStorage()
    o = Orchestrator(s)

    id = ""
    def callback(task: Task) -> None:
        nonlocal id
        id = task["id"]

    o.register_on_task_completion(callback)
    o.add_task({"id": "test"})

    assert (id == "test")

