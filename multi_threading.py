import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting" + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting" + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter -= 1

# chreate new thread
thread1 = myThread(1, "Thread-1", 10)
thread2 = myThread(2, "Thread-2", 10)

#start new threads
thread1.start()
thread2.start()

print("Exiting main thread")