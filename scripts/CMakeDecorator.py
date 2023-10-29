import subprocess
from functools import wraps

_lists_path = "."
_project_name = "task"
_cmake_target_name = "task"


def cmake_minimum_required(version: float = 3.22):
    return cmake_minimum_required.__name__ + "(VERSION " + str(version) + ")\n"


def project(project_name: str):
    return project.__name__ + "(" + project_name + ")\n"


def set(variable, value):
    return set.__name__ + "(" + variable + " " + str(value) + ")\n"


def add_executable(target_name: str):
    return add_executable.__name__ + "(" + target_name + ")\n"


def target_sources(target_name: str, sources_path: list):
    line = target_sources.__name__ + "(" + target_name + " PUBLIC "
    for p in sources_path:
        line += p + " "
    line += ")\n"
    return line


def init_cmake_lists():
    with open(_lists_path + "/CMakeLists.txt", 'w') as c:
        c.write(cmake_minimum_required(3.22))
        c.write(project(_project_name))
        c.write(add_executable(_cmake_target_name))
        c.write(target_sources(_cmake_target_name, [""]))


# TODO: add try-except, logs
def cmake(mode):
    def _decorator(task_cmd):
        """
        cmake config, build and run the task if build successfully
        record the result, catch the exceptions, print them in table
        :param task_cmd: task.run()
        :return: decoration function
        """

        @wraps(task_cmd)
        def _wrapper(*args, **kwargs):
            zipped = task_cmd(*args, **kwargs)
            if mode == "config":
                cmake_lists = _lists_path + "/CMakeLists.txt"
                with open(cmake_lists, 'r') as c:
                    content = c.readlines()
                content[-1] = target_sources(_cmake_target_name, [zipped["path"]])
                with open(cmake_lists, 'w') as c:
                    c.writelines(content)
            print(zipped["cmd"])
            p = subprocess.Popen(zipped["cmd"], shell=True, stdout=subprocess.PIPE)
            output, err = p.communicate()
            print('-' * 100)
            print(output)
            print(err)

        return _wrapper

    return _decorator