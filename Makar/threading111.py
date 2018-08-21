
# Потік в Python - Плюси:

#     Потік може значно поліпшити швидкість обчислень на багатопроцесорних або багатоядерних системах, 
#     ак як кожен процесор або ядро ​​обробляє окремий потік одночасно.
#     Потік дозволяє програмі залишатися здатною на реакцію
#     в той час як один потік чекає введення, 
#     інший працює як графічний інтерфейс. Це твердження справедливо 
#     як для багатопроцесорних або однопроцесорних систем.
#     Всі потоки процесу мають доступ до своїх глобальних змінних. 
#     Якщо глобальна змінна змінюється в одному потоці, 
#     то видима і для інших потоків також. Потік може також мати 
#     свої власні локальні змінні.

# Потік в Python - Мінуси:
#     На однопроцесорній системі, багатопоточність не впливає на швидкість обчислень. 
#     Насправді, продуктивність системи може знизитися 
#     через накладних витрат на управління потоками.
#     Синхронізація необхідна, щоб уникнути взаємного 
#     виключення при доступі до загальних ресурсів процесу. 
#     Це безпосередньо призводить до додаткової пам'яті і завантаження процесора.
#     Потік збільшує складність програми, таким чином, також робить її важким для налагодження.

# Python пропонує два модуля для реалізації threads в програмах.

#     модуль <thread> - вважається фуокціонально орієнтованим і застарілим.

#     модуль <threading> - вважається обєктноорієнтованим.
    



# є два шляхи найчастіше юзабельних шляхів для створення потоків

from threading import Thread
from random import randint
import time
class MyThread(Thread):
    def __init__(self, val):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = val
    def run(self):
        for i in range(1, self.val):
            print('Value %d in thread %s' % (i, self.getName()))
            # Sleep for random time between 1 ~ 3 second
            secondsToSleep = randint(1, 5)
            print('%s sleeping fo %d seconds...' % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)
# Run following code when the program starts
   # Declare objects of MyThread class
my_thread_obj_one = MyThread(4)
my_thread_obj_one.setName('Thread 1')
my_thread_obj_two = MyThread(4)
my_thread_obj_two.setName('Thread 2')
# Start running the threads!
my_thread_obj_one.start()
my_thread_obj_two.start()
# Wait for the threads to finish...
my_thread_obj_one.join()# як даний (гобальний потік) блокується і чекає завершення поточного потоку
my_thread_obj_two.join()

print('Main Terminating...')

# Thread-Local Data / Thread-Global Data

class MyThread(Thread):
    a = 123
    def __init__(self, val):
        ''' Constructor. '''
        Thread.__init__(self)
        self.val = val
    def run(self):
        for i in range(1, self.val):
            print('Value %d in thread %s' % (i, self.getName()))
            self.a += i
            print('%s added %d to %d' % (self.getName(), i, self.a))
# Run following code when the program starts
   # Declare objects of MyThread class
my_thread_obj_one = MyThread(4)
my_thread_obj_one.setName('Thread 1')
my_thread_obj_two = MyThread(4)
my_thread_obj_two.setName('Thread 2')
# Start running the threads!
my_thread_obj_one.start()
my_thread_obj_two.start()
# Wait for the threads to finish...
my_thread_obj_one.join()# як даний (гобальний потік) блокується і чекає завершення поточного потоку
my_thread_obj_two.join()



# thread.start()

# Починає роботу потоку.
# Це метод повинно бути викликано не більше одного разу на об'єкт потоку.
# Він організовує ресурси для виклику методу run () об'єкта
# в окремому потоці керування

# run ()

#     Метод, що відображає логіку потоку.

#     Можна замінити цей метод у підкласі. 
#     Метод standard run () викликає об'єкт, який викликається, 
#     переданий конструктору об'єкта як цільовий аргумент, якщо такий є, 
#     з послідовними та аргументами ключового слова, 
#     взятими з аргументів args та kwargs, відповідно.


# join (timeout = none)

#     Лочить потік в якому викликаний, доки потік до якого викликаний не закінчиться.
#     Це блокує виклик потоку, доки не закінчиться той потік, який приєднується до методу join () 
#     або зазвичай або через невикористоване ексепшен - або до тих пір, 
#     поки не відбудеться необов'язковий таймаут.

#     Коли аргумент timeout присутній, а не None, він має бути float, що визначає таймаут 
#     операції в секундах (або їх частках). Оскільки join () завжди повертає None, 
#     вам слід викликати is_alive () після приєднання (), 
#     щоб вирішити, чи стався тайм-аут - якщо потік ще живий, виклик join () закінчився.

#     Якщо аргумент таймауту відсутній, операція блокується, доки потік не закінчиться.

#     Потік можна приєднувати () кілька разів.

#     join () піднімає RuntimeError, якщо буде зроблена спроба приєднатись 
#     до поточного потоку, 



    # getName()

    # setName()

    # is_alive()

    # get_ident()