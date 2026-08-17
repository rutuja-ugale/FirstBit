from abc import ABC, abstractmethod

class Addition(ABC):

    @abstractmethod
    def add(self):
        pass


class Demo(Addition):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("Addition =", self.a + self.b)


obj = Demo(10, 20)
obj.add()