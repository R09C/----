class Task:
    def __init__(self, description):
        """Инициализирует задачу с описанием и статусом 'Не выполнена'."""
        self.description = description
        self.status = "Не выполнена"

    def get_description(self):
        """Возвращает описание задачи."""
        return self.description

    def get_status(self):
        """Возвращает статус задачи."""
        return self.status

    def mark_completed(self):
        """Отмечает задачу как выполненную."""
        self.status = "Выполнена"

    def display_details(self):
        """Возвращает строковое представление деталей задачи для отображения."""
        return f"Описание: {self.description}\nСтатус: {self.status}"

    def get_task_type(self):
        """Возвращает тип задачи (по умолчанию 'Обычная')."""
        return "Обычная"  # Тип задачи по умолчанию

    def get_specific_data(self):
        """Возвращает словарь для хранения специфических данных задачи."""
        return {}  # Возвращает словарь для специфических данных

    def set_specific_data(self, data):
        """Устанавливает специфические данные задачи из словаря."""
        pass  # Устанавливает специфические данные

    def __str__(self):
        """Возвращает строковое представление задачи для списка задач."""
        return f"[{self.get_task_type()}] {self.description} - {self.status}"
