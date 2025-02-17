 
from ..task import Task

class DeadlineTask(Task):
    def __init__(self, description, deadline):
        """Инициализирует задачу с дедлайном."""
        super().__init__(description)
        self.deadline = deadline

    def get_deadline(self):
        """Возвращает дедлайн задачи."""
        return self.deadline

    def display_details(self):
        """Добавляет информацию о дедлайне к деталям задачи."""
        return f"{super().display_details()}\nДедлайн: {self.deadline}"

    def get_task_type(self):
        """Возвращает тип задачи 'С дедлайном'."""
        return "С дедлайном"

    def get_specific_data(self):
        """Добавляет дедлайн к специфическим данным задачи."""
        data = super().get_specific_data()
        data["deadline"] = self.deadline
        return data

    def set_specific_data(self, data):
        """Устанавливает дедлайн из специфических данных."""
        super().set_specific_data(data)
        self.deadline = data.get("deadline", "")

    def __str__(self):
        """Добавляет информацию о дедлайне к строковому представлению задачи."""
        return f"[{self.get_task_type()}] {self.description} - {self.status} (Дедлайн: {self.deadline})"
