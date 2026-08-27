# Using Thread
# example pizza and chap
from threading import Thread
from time import sleep

class Pizza(Thread):
    def run(self):
        for i in range(5):
            print("Pizza 🍕")
            sleep(1)

class Chap(Thread):
    def run(self):
        for i in range(5):
            print("Burger 🍔")
            sleep(1)

f1 = Pizza()
f2 = Chap()
# f1.start()
f2.start()
# f1.join()
f1.run()
f2.join()
print('Sub Thread Run Ho Gaye...!!🎉🎈')