from .taskFactory import TaskFactory
from ..task import Task
from ..subentity.deadLineTask import DeadlineTask
from ..subentity.shoppingTask import ShoppingTask


class ConcreteTaskFactory(TaskFactory):
    def create_task(self, task_type, **kwargs):
        description = kwargs.get("description", "")
        if task_type == "Обычная":
            return Task(description)
        elif task_type == "С дедлайном":
            deadline = kwargs.get("deadline", "")
            return DeadlineTask(description, deadline)
        elif task_type == "Покупка":
            shopping_list = kwargs.get("shopping_list", [])
            return ShoppingTask(description, shopping_list)
        else:
            raise ValueError(f"Неизвестный тип задачи: {task_type}")
