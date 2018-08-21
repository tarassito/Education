# Деякі потоки виконують фонові завдання, 
# наприклад, відправляючи 
# виконуючи періодичну збирання сміття, 
# або що завгодно. Вони корисні лише тоді, коли працює основна програма, 
# і їх можна вбити, коли інші, не демон, потоки вийшли.

# Без потоків daemon, вам доведеться стежити за ними і 
# повідомити їм, щоб вони вийшли, перш ніж ваша програма може повністю вийти. 
# Встановивши їх як потоки daemon, ви можете дозволити їм запустити і забути про них, 
# і коли ваша програма закриється, всі потоки daemon будуть автоматично вбиті.



import sys
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    # time.sleep(1)
    f = open("abc.txt", "a")
    f.write("!!!!!!") 
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    f = open("abc.txt", "a")
    f.write("abc!") 
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
# t.join()
# d.join()

