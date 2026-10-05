

from datetime import date
from typing import Optional

from typing_extensions import Literal

from pydantic import BaseModel
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    status: str = "Not Started"  # Default value for status
    # Using Literal for specific string values
    priority: Literal["High", "Medium", "Low"]
    description: Optional[str] = None  # Optional field for description
    due_date: Optional[date] = None  # Optional field for due date

    def is_overdue(self):
        return self.due_date is not None and self.due_date < date.today()

    def is_completed(self):
        return self.status == "Completed"
