import time
import sys
import multiprocessing

def ncount(n) :
    while n > 0 : n -= 1

repnum = 10000000
thrnum = 2

print("число процесорів (ядер) = {0:d}".format(multiprocessing.cpu_count()))
print("Python версія {0:s}".format(sys.version))
print("число процесів {0:d}".format(thrnum))
print("число циклів {0:d}".format(repnum))

print("============ послідовне виконання ============")
clc = time.time()
for i in range(thrnum) : ncount(repnum)
clc = time.time() - clc
print("час {0:.2f} секунд".format(clc))

print("=============== модуль multiprocessing ==============")
parms = []
for n in range(thrnum) :
    parms.append(repnum)
multiprocessing.freeze_support()
pool = multiprocessing.Pool(processes = thrnum, )
clc = time.time()
pool.map( ncount, parms )
clc = time.time() - clc
print("час {0:.2f} секунд".format( clc ))

# число процесорів (ядер) = 4
# Python версія 3.6.1 (default, Jun  4 2018, 14:53:12)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)]
# число процесів 2
# число циклів 10000000
# ============ послідовне виконання ============
# час 1.28 секунд
# =============== модуль multiprocessing ==============
# час 0.90 секунд
