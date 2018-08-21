# Lock Objects

# Примітивний замок - це примітив синхронізації, 
# який не є власністю певної нитки при блокуванні. 
# У Python це в даний час доступний найменший рівень 
# примитиву синхронізації, який реалізується безпосередньо 
# модулем розширення _thread.

######
#Lock#
######


import threading
import time
import logging
import random


# lock = threading.Lock()

# def func():
#     lock.acquire() # set lock
#     time.sleep(2)
#     print('asd')
#     lock.release()

# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t1.start()
# lock.acquire()
# t2.start()  
# # перший потік прінтане а другий ні так як до Lock можна доступитися і знову залочити.  



# # вирішення: оголошувати Lock в межах класу або використовувати RLock.
# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-9s) %(message)s',)
                    
# class Counter(object):
#     def __init__(self, start = 0):
#         self.lock = threading.Lock()
#         self.value = start
#     def increment(self):
#         logging.debug('Waiting for a lock')
#         self.lock.acquire()
#         try:
#             logging.debug('Acquired a lock')
#             self.value = self.value + 1
#         finally:
#             logging.debug('Released a lock')
#             self.lock.release()

# def worker(c):
#     for i in range(2):
#         r = random.random()
#         logging.debug('Sleeping %0.02f', r)
#         time.sleep(r)
#         c.increment()
#     logging.debug('Done')

# if __name__ == '__main__':
#     counter = Counter()
#     for i in range(2):
#         t = threading.Thread(target=worker, args=(counter,))
#         t.start()

#     logging.debug('Waiting for worker threads')
#     main_thread = threading.currentThread()
#     print('all threads')
#     print(threading.enumerate())
#     for t in threading.enumerate():
#         if t is not main_thread:
#             t.join()
#     logging.debug('Counter: %d', counter.value)

# output
# (Thread-1 ) Sleeping 0.64
# (Thread-2 ) Sleeping 0.22
# (MainThread) Waiting for worker threads
# all threads
# [<_MainThread(MainThread, started 140180866180864)>, <Thread(Thread-1, started 140180831921920)>, <Thread(Thread-2, started 140180753217280)>]
# (Thread-2 ) Waiting for a lock
# (Thread-2 ) Acquired a lock
# (Thread-2 ) Released a lock
# (Thread-2 ) Sleeping 0.43
# (Thread-1 ) Waiting for a lock
# (Thread-1 ) Acquired a lock
# (Thread-1 ) Released a lock
# (Thread-1 ) Sleeping 0.33
# (Thread-2 ) Waiting for a lock
# (Thread-2 ) Acquired a lock
# (Thread-2 ) Released a lock
# (Thread-2 ) Done
# (Thread-1 ) Waiting for a lock
# (Thread-1 ) Acquired a lock
# (Thread-1 ) Released a lock
# (Thread-1 ) Done
# (MainThread) Counter: 4


########
# RLock#
########

# RLock використовується для безпечного блокування та у випадках рекурсії

# class X:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.lock = threading.RLock()

#     def changeA(self):
#         with self.lock:
#             self.a = self.a + 1
#             print(self.a)

#     def changeB(self):
#         with self.lock:
#             self.b = self.b + self.a
#             print(self.b)


#     def changeAandB(self):
#         # you can use chanceA and changeB threadsave!
#         with self.lock:
#             self.changeA() # a usual lock would block in here
#             self.changeB()
# a = X()            
# t1 = threading.Thread(target=a.changeAandB)
# t2= threading.Thread(target=a.changeAandB)
# t1.start()
# t2.start()



lock = threading.RLock()
def a(n):
     with lock:
        print(n)
        n-=1
        if n>0:
            a(n)
        return
t1 = threading.Thread(target=a, args=(52,))
t1.start()
