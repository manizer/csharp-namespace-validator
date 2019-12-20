import os

class BaseValidator:
    def __init__(self):
        dirpath = os.getcwd()
        self.base_path = dirpath

    def validate(self):
        pass