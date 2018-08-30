# A “greenlet” is a small independent pseudo-thread.
# You work with greenlets by jumping execution between them.

# Гринлеты переключаются когда управление явно отдается,
# либо когда производится I/O операция

# Гринлеты могут выполняться лишь на одном CPU и хороши для программ, производяших I/O операции

# Для гринлетов не существует возможности, когда два гринлета осуществляются доступ к одному и
# тому объекту в памяти в одно и то же время, так что никаких race conditions.

from greenlet import greenlet
from time import sleep

def test1():
   # while True:
       print(1)
       sleep(4)
       gr2.switch(4)
       print(3)
       gr2.switch()

def test2(val=0):
   # while True:
       print(2)
       gr1.switch()
       print(val)
       gr1.switch()

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
