import os

class Utils:
    @staticmethod
    def get_cwd() -> str:
        cwd = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        return cwd
