from validator.validator import Validator
from validator.helper.namespace_validator import NamespaceValidator
import os

class ModelValidator(Validator):
    def __init__(self):
        Validator.__init__(self)
        self.folder_name = "Model"
        self.folders_to_check = ["DTO", "Data", "Subdomains"]

    def validate(self):
        for folder_to_check in self.folders_to_check:
            path = os.path.join(self.base_path, self.folder_name, folder_to_check) 
            NamespaceValidator(path, self.folder_name).validate_namespace()