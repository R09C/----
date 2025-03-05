from ..task import Task


class DeadlineTask(Task):
    def __init__(self, description, deadline):

        super().__init__(description)
        self.deadline = deadline

    def get_deadline(self):

        return self.deadline

    def display_details(self):

        return f"{super().display_details()}\nДедлайн: {self.deadline}"

    def get_task_type(self):

        return "С дедлайном"

    def get_specific_data(self):

        data = super().get_specific_data()
        data["deadline"] = self.deadline
        return data

    def set_specific_data(self, data):

        super().set_specific_data(data)
        self.deadline = data.get("deadline", "")

    def __str__(self):

        return f"[{self.get_task_type()}] {self.description} - {self.status} (Дедлайн: {self.deadline})"
