from orchestrator.storage.storage import LocalStorage


def test_local_get_put():
    payload = {"id": "test case"}

    LocalStorage.put(payload)
    res = LocalStorage.get("test case")
    
    assert (res == payload)

def test_local_has_key():
    payload = {"id": "test case"}

    LocalStorage.put(payload)
    good = LocalStorage.has_task("test case")
    bad = LocalStorage.has_task("non existant")

    assert(good)
    assert(not bad)

def test_local_remove():
    payload = {"id": "test case"}

    LocalStorage.put(payload)
    before = LocalStorage.has_task("test case")
    LocalStorage.delete_task("test case")
    after = LocalStorage.has_task("test case")

    assert(before)
    assert(not after)
