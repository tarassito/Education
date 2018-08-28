# -*- coding: utf-8 -*-

# GIL - гарантує, що тільки один потік працює в інерпретаторі в данний момент часу.
#  Для чого? Тому що є проблема потоків і полягає в тому , що вони одночасно можуть звертатися до пам'яті.
# (Picture Thread problems)

# GIL гарантує що потік буде засинати і просипатися в правильному місці.
# А саме не під час виконання внутрішнього коду, коли він працює з памяттю.
# Переключається на інший потік після виконання тіку.

# тік це шось типу інструкція інтерпретатора. нема специфікації.
# Деякі інструкції замайють 1 тік, деякі більше.(Picture What is tick)

# До версії 3.2 CPU операції роблять check кожні 100 тіків.(sys.getcheckinterval) - (Picture Thread execution CPU / IO)
#  Під час check GIL вивільняється і його може захопити інший потік.

# є проблема , наприклад a in xrange (10**8) - це теж один тік. І він може блокувати потік.
# У версії 3.2 не 100 тіків , а 5 мс(sys.getwitchinterval)

import time
from threading import Thread

COUNT = 50000000


def countdown(n):
    while n>0:
        n -= 1


# start = time.time()
# countdown(COUNT)
# end = time.time()
# print('Time taken in seconds -', end - start)
#
# t1 = Thread(target=countdown, args=(COUNT//2,))
# t2 = Thread(target=countdown, args=(COUNT//2,))
# # t3 = Thread(target=countdown, args=(COUNT//3,))
# # t4 = Thread(target=countdown, args=(COUNT//4,))
# start = time.time()
# t1.start()
# t2.start()
# # t3.start()
# # t4.start()
# t1.join()
# t2.join()
# # t3.join()
# # t4.join()
# end = time.time()
# print('Threads time taken in seconds -', end - start)

############################################
#  1 ядро (Linux)                   Час    #
#   послідовно -------------------> 1.84c  #
#   2 потоки ---------------------> 1.73c  #
#   3 потоки ---------------------> 1.86c  #
#   4 потоки ---------------------> 1.95c  #
#  2 ядра (Linux)                          #
#   послідовно -------------------> 1.45c  #
#   2 потоки ---------------------> 1.87c  #
#   3 потоки ---------------------> 2.19c  #
#   4 потоки ---------------------> 2.51c  #
############################################


# Дивна ситуація чим більше потоків і чим більше ядер, тим довше виконується операції. Чому так відбувається?
# Проблема в тому що виникає конкуренція потоків за GIL,вони пробують захопити GIL і тим самим генерують зайві операції.
# Візуалізація цього процесу тут - http://dabeaz.blogspot.com/2010/01/python-gil-visualized.html або
# http://www.dabeaz.com/GIL/



def io():
    start = time.time()
    number = input("Enter a number")
    print("Number: ", number)
    end = time.time()
    print('Time in io -', end - start)

def foo():
    start = time.time()
    print('start: ', start)
    for a in range(10**8):
        pass
    end = time.time()
    print('end: ', end)
    print('Time in foo -', end - start)


start = time.time()
t1 = Thread(target=countdown, args=(COUNT*3,))
t2 = Thread(target=io)
# t1 = Thread(target=foo)

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('Time taken to finish all threads in seconds -', end - start)


# Приклад 1. Запускаємо з t1=countdown. І бачимо як чудово працює багатопоточність. Поки декрементується число , ми
# присвоїли число змінні number.
# Приклад 2. Запускаємо з t1=foo. І бачимо як цей довгий тік блокує інший процес.
# Приклад 3. Запускаємо в python3.

# Ще раз нагадаю, GIL нормально працює з І/О операціями, які одразу віддають GIL , коли починають чекати на дані.
# Проблеми виникають з CPU операціями, коли ми використовуємо багато ядер, бо потоками керує ОС, яка
# маючі вільні ядра, пробує захопити GIL для інших потоків. І тим самим породжує зайві процеси.
# Щоб цього уникнути можна використовувати бібліотеки або багатопроцесінг.

# GIL можна відключити. Є реалізації пайтона, які не мають GIL - Jython and IronPython
# якщо відключиш, то зменшеить швидкість виконання однопоточних програм, не зможеш інтегруватися з C бібліотеками,
#  які зазвичай не є безпечні для потоків(not thread-safe).

# Поза кадром
# Коли ми нажимаємо CTRL+C, check робиться через 1 тік, до поки не попадемо в головний потік, де потік згорнеться.


