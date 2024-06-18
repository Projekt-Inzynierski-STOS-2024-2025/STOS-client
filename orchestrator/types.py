from collections.abc import Callable


type Task = dict[str, str]
type TaskHandler = Callable[[Task], None]
