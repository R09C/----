from ..task import Task


class ShoppingTask(Task):
    def __init__(self, description, shopping_list):
        """Инициализирует задачу-покупку со списком покупок."""
        super().__init__(description)
        self.shopping_list = shopping_list

    def get_shopping_list(self):
        """Возвращает список покупок."""
        return self.shopping_list

    def display_details(self):
        """Добавляет список покупок к деталям задачи."""
        return f"{super().display_details()}\nСписок покупок: {', '.join(self.shopping_list)}"

    def get_task_type(self):
        """Возвращает тип задачи 'Покупка'."""
        return "Покупка"

    def get_specific_data(self):
        """Добавляет список покупок к специфическим данным задачи."""
        data = super().get_specific_data()
        data["shopping_list"] = self.shopping_list
        return data

    def set_specific_data(self, data):
        """Устанавливает список покупок из специфических данных."""
        super().set_specific_data(data)
        self.shopping_list = data.get("shopping_list", [])

    def __str__(self):
        """Добавляет список покупок к строковому представлению задачи."""
        return f"[{self.get_task_type()}] {self.description} - {self.status} (Покупки: {', '.join(self.shopping_list)})"
