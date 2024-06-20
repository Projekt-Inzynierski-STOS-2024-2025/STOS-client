from orchestrator.orchestrator import Orchestrator

__instance: Orchestrator = Orchestrator()

def get_instance() -> Orchestrator:
    return __instance

