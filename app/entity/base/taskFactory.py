from abc import ABC, abstractmethod


class TaskFactory(ABC):  
    @abstractmethod  
    def create_task(self, task_type, **kwargs):
        pass



