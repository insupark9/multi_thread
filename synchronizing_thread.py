import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        print("Starting" + self.name)
        # get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # free lock to release next thread
        threadLock.release()

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

# create new threads
thread1 = myThread(1, "thread-1", 10)
thread2 = myThread(2, "thread-2", 10)

# start new threads
thread1.start()
thread2.start()

# add threads to thread list
threads.append(thread1)
threads.append(thread2)

# wait for all threads to complete
for t in threads:
    t.join()

print("Exiting main thread")