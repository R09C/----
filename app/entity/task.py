class Task:
    def __init__(self, description):

        self.description = description
        self.status = "Не выполнена"

    def get_description(self):

        return self.description

    def get_status(self):

        return self.status

    def mark_completed(self):

        self.status = "Выполнена"

    def display_details(self):

        return f"Описание: {self.description}\nСтатус: {self.status}"

    def get_task_type(self):

        return "Обычная"

    def get_specific_data(self):

        return {}

    def set_specific_data(self, data):

        pass

    def __str__(self):

        return f"[{self.get_task_type()}] {self.description} - {self.status}"
