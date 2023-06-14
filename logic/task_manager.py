import datetime
from enum import Enum

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Categories(Enum):
    FINANCES = 1
    FAMILY = 2
    MEETINGS = 3
    WORK = 4
    HOME = 5
    SCHOOL = 6

class Task:
    def __init__(self, task_id: int, title: str, category: Categories, description: str, priority: Priority, deadline: datetime, user_login: str):
        self.task_id = task_id
        self.title = title
        self.category = category
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.user_login = user_login

    def __str__(self) -> str:
        return f"{self.title}\t    \t    {self.priority.name}       \t  {self.deadline}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_tasks(self, new_tasks):
        self.tasks.extend(new_tasks)

    def remove_task(self, task: Task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def get_tasks_sorted_by_priority(self):
        return sorted(self.tasks, key=lambda task: (task.priority.value, task.deadline), reverse = False)
    
    def get_tasks_sorted_by_deadline(self):
        return sorted(self.tasks, key=lambda task: task.deadline, reverse = False)