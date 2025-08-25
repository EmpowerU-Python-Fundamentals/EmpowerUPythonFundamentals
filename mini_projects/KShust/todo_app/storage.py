import json
import os
from typing import List
from models import Task

FILENAME = os.path.join(os.path.dirname(__file__), "tasks.json")

def save_tasks(tasks: List[Task]):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f)

def load_tasks() -> List[Task]:
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            try:
                raw = json.load(f)
                if isinstance(raw, list):
                    tasks: List[Task] = []
                    for item in raw:
                        if isinstance(item, dict):
                            tasks.append(Task.from_dict(item))
                        else:
                            tasks.append(Task(name=str(item)))
                    return tasks
                return []
            except Exception:
                return []
    return []
