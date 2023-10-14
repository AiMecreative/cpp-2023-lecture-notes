import os
from Task import Task


class Student(object):
    def __init__(self, folder_path: str, name: str):
        # e:\\path\\to\\student -> name = student
        self.folder_path = folder_path
        self.name = name
        self.task_list = list()
        self.submit_num = 0

    def load(self):
        for task in os.listdir(self.folder_path):
            self.task_list.append(Task(task_name=task, abs_path=self.folder_path + "/" + task))
            self.submit_num += 1
