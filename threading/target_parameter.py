from threading import Thread
from time import sleep


def whole_numbers():
    for i in range(15):
        print(i)

# Now, the whole_numbers is being executed from other thread.
thread_one = Thread(target=whole_numbers)
thread_one.start()

# Sleep help to print name of the thread at last.
sleep(2)
print(thread_one.getName())
