from concurrent.futures import ThreadPoolExecutor
from time import sleep

def return_after_5_secs(message):
    sleep(5)
    print(message)
    return message

pool = ThreadPoolExecutor(7)

future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
print(future.done())
print(future.result())
