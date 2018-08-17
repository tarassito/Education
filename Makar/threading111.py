import threading

# The multithreading library is lightweight, 
# shares memory, responsible for responsive UI and is u
# sed well for I/O bound applications. However, 
# the module isn’t killable and is subject to the GIL


from datetime import datetime


def calc_square(number):
    print('Square {}'.format(number * number))

def calc_quad(number):
    print('Quad {}'.format(number * number * number * number))
if __name__ == "__main__":
    number = 10000
    thread1 = threading.Thread(target=calc_square, args=(number,))
    thread2 = threading.Thread(target=calc_quad, args=(number,))
    # Will execute both in parallel
    start = datetime.now()
    thread1.start()
    thread2.start()
    # Joins threads back to the parent process, which is this
    # program
    thread1.join()   #поток, который вызывает этот метод, 
    # приостанавливается, ожидая завершения потока, чей метод вызван.
    thread2.join()
    stop = datetime.now()
    print(stop-start)


