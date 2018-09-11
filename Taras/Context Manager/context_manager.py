# -*- coding: utf-8 -*-

# Переваги контекстного менеджера:
# 1. усуває потребу в повторені коду по захоплення і відпуску обєкту.(DRY принцип)
# 2. запобігає помилкам при роботі з файлами, сокетами, замками, бд.
# 3. полегшує рефакторинг - наслідок DRY принципа
# 4. гарантує виконання entry, exit

# Без менеджера:
# Пайтон вміє автоматично закривати файли, але працює це не надійно. Файли треба закривати вручну.
# Багато відкритих процесів займають більше памяті,повільніше виконуються програми.Плюс к-ть відкритих процесів обмежена

# files = []
# for x in range(1000000):
#     files.append(open('foo.txt', 'w'))
#     IOError: [Errno 23] Too many open files in system: 'foo.txt'


# Зміни не попадуть у файл допоки він не закритий. Тому якщо скрипт записує, а потім читає, то він не побачить змін.
# Часто просто забувають закривати.

import time

# Приклад демонструє, що текст зявляється лише після close().

# fw = open("./without.txt", "w")
# fw.write("Enter text file. ")
# print("First sleep")
# time.sleep(10)
# fw.write("Wake up")
# fw.close()
#
# Щоб кожен раз не викликати close():
# with open("./with.txt", "w") as fp:
#     fp.write("Hello, World")
# print("Second sleep")
# time.sleep(10)


# Приклад того, що деструктор в Пайтоні викликається лише тоді, коли немає посилань на обєкт. Тому покладатися на
#  закриття файлів пайтоном ненадійно.
class Hello:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("deleted", self.name)


# h1 = Hello('h1')
# h2 = Hello('h2')
# h3 = Hello('h3')
# z = h3
# x = h3
# del h1
# del h2
# del h3 # деструктор h3 не викликався
# print("exit-1")

# deleted h1
# deleted h2
# exit-1
# deleted h3

# Приклад створення власного контекст менеджера, і хід виконання його меджік методів
# class ConManager:
#     def __exit__(self, exp_type, exp_value, traceback):
#         print("I'm in the exit block")
#
#     def __enter__(self):
#         print("I'm in the enter block")
#
#
# with ConManager():
#     print('my code')
#
# print("exit-2")

# I'm in the enter block
# my code
# I'm in the exit block
# exit-2


# Приклад контекстного менеджера з перевизначенням __enter__ та __exit__
class Open(object):
    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def __enter__(self):
        try:
            self.fp = open(self.file, self.flag)
        except ValueError:
            self.fp = open(self.file, "r")
        return self.fp

    def __exit__(self, exp_type, exp_value, exp_tr):
        if exp_type is RuntimeError:
            self.fp.close()
            print("my runtime error ")
            return True
        self.fp.close()

with Open("test.txt", "rrrrrr") as fp:
    print(fp.readline())
    raise RuntimeError

# Hello hello
# my runtime error

op = Open("test.txt", 'w')
with op as file:
    file.write("I use objects here")

# Приклад створення контекст менеджера, використовуючи модуль зі стандартної бібліотеки
# from contextlib import contextmanager
# @contextmanager
# def managed_file(name):
#     try:
#         f = open(name, 'w')
#         yield f
#     finally:
#         f.close()
#
# with managed_file('hi.txt') as file:
#     file.write("I like use decoreators")


# Приклад використання контекст менеджера з замком
# from threading import Lock
# lock = Lock()
#
# def do_something_dangerous():
#     with lock:
#         raise Exception('oops I forgot this code could raise exceptions')
#
# try:
#     do_something_dangerous()
# except:
#     print('Got an exception')
# lock.acquire()
# print('Got here')