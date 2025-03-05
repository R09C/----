from ..task import Task


class ShoppingTask(Task):
    def __init__(self, description, shopping_list):

        super().__init__(description)
        self.shopping_list = shopping_list

    def get_shopping_list(self):

        return self.shopping_list

    def display_details(self):

        return f"{super().display_details()}\nСписок покупок: {', '.join(self.shopping_list)}"

    def get_task_type(self):

        return "Покупка"

    def get_specific_data(self):

        data = super().get_specific_data()
        data["shopping_list"] = self.shopping_list
        return data

    def set_specific_data(self, data):

        super().set_specific_data(data)
        self.shopping_list = data.get("shopping_list", [])

    def __str__(self):

        return f"[{self.get_task_type()}] {self.description} - {self.status} (Покупки: {', '.join(self.shopping_list)})"
