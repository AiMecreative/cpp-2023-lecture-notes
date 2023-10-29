from CMakeDecorator import cmake, redirect


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

    @redirect
    @cmake("config")
    def config(self, config_cmd):
        print(config_cmd)
        return {"cmd": config_cmd, "path": self.abs_path}

    @redirect
    @cmake("build")
    def build(self, build_cmd):
        print(build_cmd)
        return {"cmd": build_cmd}

    @redirect
    def run(self, exe: str, fill_params: bool = True):
        return {"cmd": exe, "fill_params": fill_params}
