import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from entity.base.concreteTaskFactory import ConcreteTaskFactory
from entity.base.concreteTaskFactory import WorkTaskFactory


class WorkTaskManagerGUI_Factory:

    def __init__(self, root):

        self.root = root
        root.title("Менеджер Основных Задач (Фабричный Метод)")

        self.task_factory_regular = WorkTaskFactory()
        self.tasks = []
        self.task_var = tk.StringVar(value=[str(task) for task in self.tasks])
        self.task_listbox = tk.Listbox(
            root, listvariable=self.task_var, height=10, width=50
        )
        self.task_listbox.pack(pady=10, padx=10)
        self.task_listbox.bind("<Double-Button-1>", self.show_task_details)

        self.add_button = ttk.Button(
            root, text="Добавить рабочую задачу", command=self.open_add_task_window
        )
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = ttk.Button(
            root, text="Удалить Задачу", command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.complete_button = ttk.Button(
            root, text="Отметить выполненной", command=self.mark_task_completed
        )
        self.complete_button.pack(side=tk.LEFT, padx=5, pady=5)

    def update_task_list(self):

        self.task_var.set([str(task) for task in self.tasks])

    def open_add_task_window(self):

        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Добавить Основную Задачу")

        ttk.Label(self.add_window, text="Тип задачи:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        task_types = ["Обычная", "С дедлайном", "Покупка"]
        self.task_type_combobox = ttk.Combobox(self.add_window, values=task_types)
        self.task_type_combobox.set(task_types[0])
        self.task_type_combobox.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.add_window, text="Описание задачи:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.description_entry = ttk.Entry(self.add_window, width=40)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        self.specific_fields_frame = ttk.Frame(self.add_window)
        self.specific_fields_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.task_type_combobox.bind("<<ComboboxSelected>>", self.show_specific_fields)
        self.show_specific_fields()

        ttk.Button(self.add_window, text="Добавить Задачу", command=self.add_task).grid(
            row=3, column=0, columnspan=2, pady=10
        )

    def show_specific_fields(self, event=None):

        for widget in self.specific_fields_frame.winfo_children():
            widget.destroy()

        task_type = self.task_type_combobox.get()
        if task_type == "С дедлайном":
            ttk.Label(self.specific_fields_frame, text="Дедлайн (ГГГГ-ММ-ДД):").pack(
                side=tk.LEFT, padx=5
            )
            self.deadline_entry = ttk.Entry(self.specific_fields_frame, width=15)
            self.deadline_entry.pack(side=tk.LEFT)
        elif task_type == "Покупка":
            ttk.Label(
                self.specific_fields_frame, text="Список покупок (через запятую):"
            ).pack(side=tk.LEFT, padx=5)
            self.shopping_entry = ttk.Entry(self.specific_fields_frame, width=30)
            self.shopping_entry.pack(side=tk.LEFT)

    def add_task(self):

        task_type = self.task_type_combobox.get()
        description = self.description_entry.get()
        specific_data = {"description": description}

        try:
            if task_type == "С дедлайном":
                deadline_str = self.deadline_entry.get()
                datetime.strptime(deadline_str, "%Y-%m-%d")
                specific_data["deadline"] = deadline_str
            elif task_type == "Покупка":
                shopping_list_str = self.shopping_entry.get()
                specific_data["shopping_list"] = [
                    item.strip() for item in shopping_list_str.split(",")
                ]

            task = self.task_factory_regular.create_task(task_type, **specific_data)

            self.tasks.append(task)
            self.update_task_list()
            self.add_window.destroy()
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))

    def delete_task(self):

        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_list()

    def mark_task_completed(self):

        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index].mark_completed()
            self.update_task_list()

    def show_task_details(self, event):

        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            messagebox.showinfo("Детали задачи", task.display_details())
