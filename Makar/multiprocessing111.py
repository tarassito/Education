import multiprocessing
from datetime import datetime


def calc_square(number):
    print('Square {}'.format(number * number))


def calc_quad(number):
    print('Quad {}'.format(number * number * number * number))


if __name__ == "__main__":
    number = 10000

    p1 = multiprocessing.Process(target=calc_square, args=(number,))
    p2 = multiprocessing.Process(target=calc_quad, args=(number,))
    start = datetime.now()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    stop = datetime.now()
    print(stop-start)

# Square 100000000
# Quad 10000000000000000
# 0:00:00.008254
