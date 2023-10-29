import os
from Student import Student


class AutoChecker(object):
    def __init__(self, config):
        self.student_list = config["checker"]["student_list"]
        self.question_count = config["checker"]["question_count"]
        self.multi_file = config["checker"]["multi_file"]
        self.tasks_folder = config["checker"]["tasks_folder"].replace('\\', '/')

        self.exe = config["checker"]["target_exe"]
        self.workflow_config = config["workflow"]

    def next_student(self):
        print(self.tasks_folder)
        for f_name in os.listdir(self.tasks_folder):
            student = Student(self.tasks_folder + "/" + f_name, f_name)
            student.load()
            yield student

    def check_submit(self, student: Student):
        return student.submit_num == self.question_count

    def start(self):
        for student in self.next_student():
            self.check_submit(student)
            for task in student.task_list:
                task.config(self.workflow_config["cmake_config"])
                task.build(self.workflow_config["cmake_build"])
                task.run(self.exe, False)
