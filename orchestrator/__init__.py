from orchestrator.orchestrator import Orchestrator
from orchestrator.storage.storage import LocalStorage

__instance: Orchestrator = Orchestrator(LocalStorage())

def get_instance() -> Orchestrator:
    return __instance

