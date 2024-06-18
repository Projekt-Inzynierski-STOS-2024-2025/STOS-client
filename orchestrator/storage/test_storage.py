from orchestrator.storage.storage import LocalStorage


def test_local_get_put():
    s = LocalStorage()
    payload = {"id": "test case"}

    s.put(payload)
    res = s.get("test case")
    
    assert (res == payload)

def test_local_has_key():
    s = LocalStorage()
    payload = {"id": "test case"}

    s.put(payload)
    good = s.has_task("test case")
    bad = s.has_task("non existant")

    assert(good)
    assert(not bad)

def test_local_remove():
    s = LocalStorage()
    payload = {"id": "test case"}

    s.put(payload)
    before = s.has_task("test case")
    s.delete_task("test case")
    after = s.has_task("test case")

    assert(before)
    assert(not after)
