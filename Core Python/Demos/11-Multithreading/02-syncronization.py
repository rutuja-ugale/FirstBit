from threading import Thread,Lock
from time import sleep
class Withdrw(Thread):
    bal = 100
    lock = Lock()
    def run(self):
        Withdrw.lock.acquire()
        if Withdrw.bal>0:
            print(self.name,"Check Balance")
            Withdrw.bal = Withdrw.bal-2     #   98
            print(self.name,"Balance get Withdraw")
            sleep(1)
        else:
            print("Insuficent Fund")
        print(f"Remaining Amount= {Withdrw.bal}")
        Withdrw.lock.release()
t1=Withdrw()
t2=Withdrw()
t3=Withdrw()
t1.start()
t2.start()
t3.start()