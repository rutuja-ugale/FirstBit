class Trainer:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Id:{self.id},Name:{self.name}, Salary:{self.salary}"