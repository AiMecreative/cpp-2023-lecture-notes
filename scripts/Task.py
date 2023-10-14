from CMakeDecorator import cmake


class Task(object):
    """single question task, single file task"""

    def __init__(self, task_name: str, abs_path: str):
        self.name = task_name
        self.abs_path = abs_path.replace('\\', '/')
        self.score = float()
        self.result = str()
        self.finished = False

    def __str__(self):
        info = "Task {\nname: " + self.name + "\nfinished: " + str(self.finished) + "\nabs_path: " + self.abs_path
        if self.finished:
            info += "\nscore: " + str(self.score)
            info += "\nresult: " + self.result
        info += "\n}"
        return info

    @cmake("config")
    def config(self, config_cmd):
        print("abs_path: " + self.abs_path)
        return {"cmd": config_cmd, "path": self.abs_path}

    @cmake("build")
    def build(self, build_cmd):
        return {"cmd": build_cmd}
