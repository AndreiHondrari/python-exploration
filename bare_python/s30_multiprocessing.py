#!/usr/bin/python3

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super(MyThread, self).__init__()
        self.name = name
        self.delay = delay

    def run(self):
        for i in range(5):
            print(self.name + " " + str(i))
            time.sleep(self.delay)

t1 = MyThread("T1", 0.3)
t2 = MyThread("T2", 0.2)

t1.start()
t2.start()

while 1:
    time.sleep(0.1)
    if threading.activeCount() <= 1:
        break

print("FINISHED SEQ 1")

t1 = MyThread("T1", 0.3)
t2 = MyThread("T2", 0.2)

t1.start()
t2.start()

t1.join()
t2.join()

print("FINISHED SEQ 2")

print("EXITING MAIN THREAD")