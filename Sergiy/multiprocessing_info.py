# Процес - екземпляр програми під час виконання, незалежний об'єкт, якому виділені системні ресурси
# (наприклад, процесорний час і пам'ять).
# Кожен процес виконується в окремому адресному просторі: один процес не може отримати доступ до змінних і структурам даних іншого.
# Якщо процес хоче отримати доступ до чужих ресурсів, необхідно використовувати міжпроцесну взаємодію.
# Це можуть бути конвеєри, файли, канали зв'язку між комп'ютерами та багато іншого.
#
# Потік використовує той ж самий простір стеку, що і процес,
# а безліч потоків спільно використовують дані своїх станів.
# Як правило, кожен потік може працювати (читати і писати) з однієї і тієї ж області пам'яті,
# на відміну від процесів, які не можуть просто так отримати доступ до пам'яті іншого процесу.
# У кожного потоку є власні регістри і власний стек, але інші потоки можуть їх використовувати.
# Коли один потік змінює ресурс процесу, це зміна відразу ж стає видно іншим потокам цього процесу.
#
# Стек (англ. Stack) - це спеціально відведена область оперативної пам'яті для зберігання проміжних даних під час виконання програми.

import os
from multiprocessing import Process, current_process


# Функція, що приймає число і повертає 2 * число. Також прінтує назву процесу
def doubler(number):
    result = number * 2
    proc = current_process().name
    proc_id = os.getpid()
    print(f"{number} doubled to {result} by {proc} (id = {proc_id})")

import datetime
if __name__ == '__main__':
    time = datetime.datetime.now()
    numbers = [5, 10, 15, 20, 25]
    procs = []


    for number in numbers:
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()                                       # start() - стартує процес. Викликається тільки раз.
                                                           # Викликає метод об'єкта run() в окремому процеці
    for proc in procs:
        proc.join()                                        # join([timeout]) - очікує завершення процесу, тобто
                                                           # провіряє exitcode процесу. Якщо timeout не є None, а більше 0,
                                                           # то блокує на кількісь секунд в цьому аргументі.
                                                           # Цей метод може викликатись не один раз
    time_mproc = (datetime.datetime.now()-time).microseconds

    time = datetime.datetime.now()
    for number in numbers:
        doubler(number)
    time_proc = (datetime.datetime.now()-time).microseconds
    print(f"multiprocessing time = {time_mproc}")
    print(f"singleprocessing time = {time_proc}")
    print(f"Difference = {time_mproc-time_proc}")
# 10 doubled to 20 by Process-2 (id = 229)
# 15 doubled to 30 by Process-3 (id = 230)
# 5 doubled to 10 by Process-1 (id = 228)
# 20 doubled to 40 by Process-4 (id = 231)
# 25 doubled to 50 by Process-5 (id = 232)

# Для 100 чисел результати часу роботи(В мікросекундах)
# multiprocessing time = 550 000
# singleprocessing time = 18 000
# Difference = 532 000

    proc = Process(target=doubler, name="My Process", args=(3,))
    proc.start()
# 3 doubled to 6 by My Process (id = 250)

# Шляхи старту процесу
# -----spawn-----
# Вихідний процес запускає новий процес в інтерпретаторі. Дочірній процес успадкує лише ті ресурси,
# які необхідні для запуску методу process run(). Зокрема, непотрібні дескриптори файлів з батьківського процесу не будуть успадковані.
# Початок процесу з використанням цього методу є досить повільним порівняно з використанням fork або forkserver.
#
# Доступно в Unix та Windows. По замовчуванню на Windows.
#
# -----fork-----
# В батьківському процесі використовується os.fork(), щоб розгорнути інтерпретатор Python.
# Дочірній процес, коли він починається, фактично ідентичний батьківському процесу.
# Всі ресурси батьків успадковуються від дочірнього процесу. Безпечний fork багатопотокового процесу є проблематичним.
#
# Доступно лише для Unix. За замовчуванням на Unix.
#
# -----forkserver-----
# Коли програма запускає та вибирає метод запуску forkserver, починається процес сервера.
# Відтепер, коли потрібен новий процес, батьківський процес підключається до сервера і вимагає, щоб він запускав новий процес.
# Процесор серверного вилка є однопоточним, тому для нього безпечно використовувати os.fork(). Непотрібні ресурси не успадковуються.
#
# Доступні на платформах Unix, які підтримують передані файлові дескриптори над Unix pipes.
# Locks - замки
# Щоб не дати процесам конфліктувати один з одним, використовуєmся об'єкт Lock.
# Так як використовуються замки, наступний процес в рядку буде чекати, поки замок не зніметься, після чого він зможе продовжити.

# set_start_method() - цей метод дозволяє вибрати метод створення процесу

from multiprocessing import Process, Lock


def printer(item, lock):
    lock.acquire()
    print(item)
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]

    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()


# Pools
from multiprocessing import Pool


def doubler(number):
    return number * 2


if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
# Метод map() відображає результат функції кожного процесу
# [10, 20, 40]

from multiprocessing import Pool


def doubler(number):
    return number * 2


if __name__ == '__main__':
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))

# apply_async() - Повертає результуючий об'єкт
# get(timeout) - повертає результат, коли він надходить. Якщо протягом часу, зазначеного в timeout
# не надходить результат, то буде викликана TimeoutError


# Черги - Queue
# Кожного разу, коли ви використовуєте чергу, ви повинні переконатися,
# що всі елементи, які були поставлені в чергу, зрештою будуть вилучені,
# перш ніж процес буде об'єднано. В іншому випадку ви не можете бути впевнені,
# що процес, який поставив елементи в чергу, припиниться

from multiprocessing import Process, Queue

def f(q):
    q.put('X' * 1000000)                   # put() - ставить елемент в чергу

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    # p.join(timeout=2)                    # this deadlocks
    obj = queue.get()                      # get() - вилучає з черги
    print(obj)

# Канали зв'язку - pipes
# Pipe
# Повертає пару об'єктів з'єднання, з'єднаних трубою, яка за замовчуванням є двосторонньою.
# from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()

# send() - відправлення даних
# recv() - отримання даних
