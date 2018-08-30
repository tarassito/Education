import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def handle_response(response):
    if response.error:
        print("Error:", response.error)
        return False
    else:
        url = response.request.url
        data = response.body
        print('{}: {}'.format(url, len(data)))
        return True

http_client = AsyncHTTPClient()
for url in urls:
    http_client.fetch(url, handle_response)

tornado.ioloop.IOLoop.instance().start()
