from threading import Thread
from random import randint
import time
import sys


class MyThread(Thread):
    a = 123
    def __init__(self, val):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = val
    def run(self):
        for i in range(1, self.val):
            with open("demofile.txt", "a") as f:
                f.write("Now the file has one more line! \n") 
            secondsToSleep = randint(1, 5)
            print('%s sleeping fo %d seconds...' % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)
# Run following code when the program starts
   # Declare objects of MyThread class
# my_thread_obj_one = MyThread(4)
# my_thread_obj_one.setName('Thread 1')
my_thread_obj_two = MyThread(1)
my_thread_obj_two.setName('Thread 2')
my_thread_obj_two.setDaemon(True)
my_thread_obj_two.start()
my_thread_obj_two.join()

# Start running the threads!
sys.exit()
# Wait for the threads to finish...
# my_thread_obj_one.join()# як даний (гобальний потік) блокується і чекає завершення поточного потоку
# my_thread_obj_two.join()