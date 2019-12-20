from validator.validator import Validator

def check():
    Validator("Model", subfolders_to_check=["DTO", "Data", "Subdomains"]).validate()
    Validator("Repository", subfolders_to_check=["Repositories"]).validate()
    Validator("Service", subfolders_to_check=["Modules"]).validate()
    Validator("SantoLeoPayroll", subfolders_to_check=["Areas", "Container", "Controllers", "Helpers", "Middlewares", "ViewComponents", "ViewModels"]).validate()

if __name__ == "__main__":
    check()