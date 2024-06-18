from cache.cache_manager import czy_plikies, handle_completion
from orchestrator import get_instance


def main():
    print("Starting app")
    o = get_instance()
    o.register_on_task_completion(handle_completion)
    czy_plikies(o)


if __name__ == "__main__":
    main()
