from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    name: str
    status: str = "in_progress"
    deadline: datetime = None

    def mark_done(self):
        self.status = "done"

    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status,
            "deadline": self.deadline.isoformat() if self.deadline else None
        }

    @classmethod
    def from_dict(cls, data):
        name = data.get("name", "")
        status = data.get("status", "in_progress")
        deadline = data.get("deadline")
        if deadline:
            try:
                deadline = datetime.fromisoformat(deadline)
            except:
                deadline = None
        return cls(name=name, status=status, deadline=deadline)

    def display_text(self):
        if self.deadline:
            return f"{self.name} (due {self.deadline.strftime('%Y-%m-%d %H:%M')})"
        else:
            return self.name
