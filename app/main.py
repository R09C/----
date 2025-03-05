import tkinter as tk
from tkinter import ttk, messagebox
from UI.taskManagerGUI_Factory import TaskManagerGUI_Factory
from UI.taskManagerGUI_NoFactory import TaskManagerGUI_NoFactory
from UI.workTaskManagerGUI_Factory import WorkTaskManagerGUI_Factory

root = tk.Tk()


def run_with_factory():

    window_factory = tk.Toplevel(root)
    TaskManagerGUI_Factory(window_factory)


def run_without_factory():

    window_no_factory = tk.Toplevel(root)
    TaskManagerGUI_NoFactory(window_no_factory)


def run_work_factory():
    window_work_factory = tk.Toplevel(root)
    WorkTaskManagerGUI_Factory(window_work_factory)


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
ttk.Button(
    root,
    text="Запустить Менеджер задач рабочий",
    command=run_work_factory,
).pack(pady=10)

root.mainloop()
