from abc import ABC, abstractmethod

class Concatenate(ABC):

    @abstractmethod
    def concat(self):
        pass


class Demo(Concatenate):

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def concat(self):
        print("Concatenated String =", self.str1 + self.str2)


obj = Demo("Firstbit ", "Solution")
obj.concat()