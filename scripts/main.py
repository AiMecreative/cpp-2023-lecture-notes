from CMakeDecorator import init_cmake_lists
from config import init_configurations
from AutoCheker import AutoChecker

if __name__ == '__main__':
    configurations = init_configurations()
    init_cmake_lists()
    checker = AutoChecker(config=configurations)
    checker.start()
