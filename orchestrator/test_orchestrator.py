from orchestrator.orchestrator import Orchestrator, Task

def test_notify():
    is_successful: bool = False
    def callback(task: Task) -> None:
        print(task)
        nonlocal is_successful
        is_successful = True

    o = Orchestrator()

    o.register_on_task_completion(callback)
    o._notify_task_completion({"stuff": "test"})

    assert(is_successful)
