from threading import *
from time import sleep


# Extend the Thread class and override the run() method.
class Hello(Thread):

    # Define the activities inside the run() method.
    def run(self):
        for i in range(5):
            # Sets interval of 1 second between every printing of "Hello".
            sleep(1)
            print("Hello")


class Hi(Thread):
    def run(self):
        for i in range(5):
            # Sets interval of 1 second between every printing of "Hi".
            sleep(1)
            print("Hi")


# Create objects of those class who extended Thread class.
thread_one = Hello()
thread_two = Hi()

# Execute the activities by calling the start() method, not run() method. In
# background, start() method invokes run() method.
thread_one.start()
# Create interval between start() method invoking of different Thread objects.
# Make it different than 1 second to see it working(printing) parallely.
sleep(0.4)
thread_two.start()

# "Thanks for watching" is not manually associated with any thread. So, by
# default is it associated with main thread. To print it at last, the threads
# are joined with the main thread i.e. when join() is used for a particular
# thread the main thread will stop executing until the execution of joined
# thread is complete.
thread_one.join()
thread_two.join()

print("Thanks for watching.")
