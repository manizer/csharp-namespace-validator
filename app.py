from validator.model_validator import ModelValidator

def check():
    ModelValidator().validate()

if __name__ == "__main__":
    check()