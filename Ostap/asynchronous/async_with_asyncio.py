# asyncio.Future: non-blocking by design
# The asyncio.Future and the concurrent.futures.Future classes have mostly the
# same interface, but are implemented differently and are not interchangeable. PEP-3156
# — Asynchronous IO Support Rebooted: the “asyncio” Module has this to say about this
# unfortunate situation:
# In the future (pun intended) we may unify asyncio.Future and concurrent.fu
# tures.Future, e.g. by adding an __iter__ method to the latter that works with yield from.


# futures are created only as the
# result of scheduling something for execution. In asyncio, BaseEventLoop.cre
# ate_task(…) takes a coroutine, schedules it to run, and returns an asyncio.Task instance
# — which is also an instance of asyncio.Future because Task is a subclass of
# Future designed to wrap a coroutine. This is analogous to how we create concur
# rent.futures.Future instances by invoking Executor.submit(…).

# Like its concurrent.futures.Future counterpart, the asyncio.Future class provides
# .done(), .add_done_callback(…) and .results() methods, among others. The
# first two methods work as described in “Where are the futures?” on page 513,
# but .result() is very different.
# In asyncio.Future the .result() method takes no arguments, so you can’t specify a
# timeout. Also, if you call .result() and the future is not done, it does not block waiting
# for the result. Instead, an asyncio.InvalidStateError is raised.

#
# Using yield from with a future automatically takes care of waiting for it to finish,
# without blocking the event loop — because in asyncio, yield from is used to give
# control back to the event loop.

# Note that using yield from with a future is the coroutine equivalent of the functionality
# offered by add_done_callback: instead of triggering a callback, when the delayed operation
# is done the event loop sets the result of the future, and the yield from expression
# produces a return value inside our suspended coroutine, allowing it to resume.

# • You don’t need my_future.add_done_callback(…) because you can simply put
# whatever processing you would do after the future is done in the lines that follow
# yield from my_future in your coroutine. That’s the big advantage of having coroutines:
# functions that can be suspended and resumed.
# • You don’t need my_future.result() because the the value of yield from expression
# on a future is the result, e.g. result = yield from my_future.


#
# In order to execute, a coroutine must be scheduled, and then it’s wrapped in an asyn
# cio.Task. Given a coroutine, there are two main ways of obtaining a Task:
# asyncio.async(coro_or_future, *, loop=None)
# This function unifies coroutines and futures: the first argument can be either one.
# If it’s a Future or Task, it’s returned unchanged. If it’s a coroutine, async calls
# loop.create_task(…) on it to create a Task. An optional event loop may be passed
# as the loop= keyword argument; if omitted, async gets the loop object by calling
# asyncio.get_event_loop().
# BaseEventLoop.create_task(coro)
# This method schedules the coroutine for execution and returns an asyncio.Task
# object. If called on a custom subclass of BaseEventLoop, the object returned may
# be an instance of some other Task-compatible class provided by an external library,
# e.g. Tornado.

# This is similar to the taxi simulation in “The taxi fleet simulation” on page 492, where
# a main loop started several taxi processes in turn. As each taxi process yielded, the main
# loop scheduled the next event for that taxi (to happen in the future), and proceeded to
# activate the next taxi in the queue. The taxi simulation is much simpler, and you can
# easily understand it’s main loop. But the general flow is the same as in asyncio: a singlethreaded
# program where a main loop activates queued coroutines one by one. Each
# coroutine advances a few steps, then yields control back to the main loop, which then
# activates the next coroutine in the queue.

import re
import asyncio
import aiohttp
from picture import save_img, show, main, site_t, site


async def get_img(url):
    async with aiohttp.request('GET', url) as resp:
        image = await resp.read()
        return image


async def download_one(url):
    if 'http' not in url:
        url = '{}{}'.format(site_t, url)
    image = await get_img(url)
    filename = re.search('/([^/]+\.(?:jpg|gif|png))', url)
    if not filename:
        filename = url[-10]
        save_img(image, filename)
        return filename
    else:
        show(url)
        save_img(image, filename.group(1))
        return filename.group(1)


def download_many(urls):
    loop = asyncio.get_event_loop()
    print(loop)
    to_do = [download_one(cc) for cc in sorted(urls)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)
