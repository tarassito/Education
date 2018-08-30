# The primary pattern used in gevent is the Greenlet, a lightweight coroutine
# provided to Python as a C extension module. Greenlets all run inside of the
# OS process for the main program but are scheduled cooperatively.

# with coroutines shedules greenlets into event loop

import gevent

def foo():
    while True:
        print('Running in foo')
        gevent.sleep(2)
        print('Explicit context switch to foo again')

def bar():
    while True:
        print('Explicit context to bar')
        gevent.sleep(1)
        print('Implicit context switch back to bar')

def serhii():
    while True:
        print('woo')
        gevent.sleep(3)
        print('hoo')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(serhii),
])
