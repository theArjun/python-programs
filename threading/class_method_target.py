from threading import *


class Sanskaar:
    def greet(self, name="Arjun"):
        print("Hello {}".format(name))


greeter = Sanskaar()
thread_one = Thread(target=greeter.greet)
thread_one.start()
