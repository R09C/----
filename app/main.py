import tkinter as tk
from tkinter import ttk, messagebox
from UI.taskManagerGUI_Factory import TaskManagerGUI_Factory
from UI.taskManagerGUI_NoFactory import TaskManagerGUI_NoFactory

root = tk.Tk()


# Кнопки для запуска версий с фабрикой и без фабрики
def run_with_factory():
    """Запускает Менеджер задач с Фабричным Методом."""
    window_factory = tk.Toplevel(root)
    TaskManagerGUI_Factory(window_factory)


def run_without_factory():
    """Запускает Менеджер задач БЕЗ Фабричного Метода."""
    window_no_factory = tk.Toplevel(root)
    TaskManagerGUI_NoFactory(window_no_factory)


ttk.Button(
    root,
    text="Запустить Менеджер задач (с Factory Method)",
    command=run_with_factory,
).pack(pady=10)
ttk.Button(
    root,
    text="Запустить Менеджер задач (БЕЗ Factory Method)",
    command=run_without_factory,
).pack(pady=10)

root.mainloop()
