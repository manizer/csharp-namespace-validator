from validator.base_validator import BaseValidator
from validator.helper.namespace_validator import NamespaceValidator
import os

class Validator(BaseValidator):
    def __init__(self, folder_name, subfolders_to_check):
        BaseValidator.__init__(self)
        self.folder_name = folder_name
        self.subfolders_to_check = subfolders_to_check

    def validate(self):
        for subfolder_to_check in self.subfolders_to_check:
            path = os.path.join(self.base_path, self.folder_name, subfolder_to_check) 
            NamespaceValidator(path, self.folder_name).validate_namespace()