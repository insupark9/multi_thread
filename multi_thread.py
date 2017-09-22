import thread
import time

# define a function for the thread
def print_time(thread_name, delay):
    count = 0

    while count < 5:
        time.sleep(delay)
        count += 1
        print(thread_name, time.ctime(time.time()))

# create two threads as follows
try:
    thread.start_new_thread(print_time, ("Thread-1", 2))
    thread.start_new_thread(print_time, ("Thread-2", 4))

except:
    print("Error: unable to start thread")

while 1:
    pass