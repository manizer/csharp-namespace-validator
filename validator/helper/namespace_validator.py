import os
from validator.validator import Validator

class NamespaceValidator(Validator):
    def __init__(self, path, expected_first_namespace_folder):
        Validator.__init__(self)
        self.path = path
        self.expected_first_namespace_folder = expected_first_namespace_folder

    def validate_namespace(self):
        self.__validate_namespace_in_folder(self.path)
        
    # recursively check for namespaces in a given folder
    def __validate_namespace_in_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".cs"):
                lines = [line.rstrip('\n') for line in open(os.path.join(folder_path, filename))]
                line_cnt = 0
                max_line_try_cnt = 200

                for line in lines:
                    if(line_cnt > max_line_try_cnt):
                        break
                    line_cnt += 1
                    if line.startswith('namespace'): 
                        namespace = line.replace('namespace', '').replace('{', '').replace('}', '').strip()
                        namespace_folder = folder_path.replace(self.base_path, '')
                        # validate namespace
                        expected_namespaces = list(filter(lambda x: (x.strip() != ""), namespace_folder.split('/'))) 
                        actual_namespaces = list(filter(lambda x: (x.strip() != ""), namespace.split('.')))
                        if(expected_namespaces != actual_namespaces):
                            print(f"Expected: {expected_namespaces}")
                            print(f"Actual: {actual_namespaces}")
                        break
            else :
                if os.path.isdir(os.path.join(folder_path, filename)):
                    self.__validate_namespace_in_folder(os.path.join(folder_path, filename))