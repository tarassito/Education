import re
from concurrent import futures
from picture import save_img, get_img, show, main, site_t


MAX_WORKERS = 100


def download_one(url):
    if 'http' not in url:
        url = '{}{}'.format(site_t, url)
    image = get_img(url)
    filename = re.search('/([^/]+\.(?:jpg|gif|png))', url)
    if not filename:
        filename = url[-10]
        save_img(image, filename)
        return filename
    else:
        show(url)
        save_img(image, filename.group(1))
        return filename.group(1)


# def download_many(cc_list):
#     workers = min(MAX_WORKERS, len(cc_list))
#     with futures.ThreadPoolExecutor(workers) as executor:
#         res = executor.map(download_one, sorted(cc_list))
#         return len(list(res))

def download_many(cc_list):
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        to_do = []
        for url in sorted(cc_list):
            future = executor.submit(download_one, url)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(url[-10], future))

        results = []

        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)

# Strictly speaking, none of the concurrent scripts we tested so far can perform downloads
# in parallel. The concurrent.futures examples are limited by the GIL, and the
# async_with_asyncio.py is single-threaded.

if __name__ == '__main__':
    main(download_many)
