class Emp:
    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary
    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getSalary(self):
        return self.__salary
    def setSalary(self, salary):
        self.__salary = salary
    def calSalary(self):
        print(f"Emp Salary = {self.__salary}")
    def display(self):
        print(f"Id = {self.__id},\t Name = {self.__name},\t Salary = {self.__salary}")