# Single threaded applications run on main thread
import threading


# current_thread() returns Threading object, so getName() is invoked to get
# name of the thread.
print("Currently running thread : ", threading.current_thread().getName())

# Comparing the threads in Program
if threading.current_thread() == threading.main_thread():
    print("Main thread is being executed.")
else:
    print("Other thread is being executed.")
