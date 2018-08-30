import os
import time
import sys
import re
import requests
from bs4 import BeautifulSoup

# site = 'https://fantasy-worlds.org/lib/'
# site = 'https://www.penguinrandomhouse.com/the-read-down/21-books-youve-been-meaning-to-read'
site = 'https://www.cbsnews.com/pictures/'
site_t = 'https://www.cbsnews.com'
# site_t = 'https://fantasy-worlds.org'
# site_t = 'https://www.penguinrandomhouse.com'

DEST_DIR = 'downloads/'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_img(url):
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(urls):
    for url in sorted(urls):
        filename = re.search('/([^/]+\.(?:jpg|gif|png))', url)
        if 'http' not in url:
            url = '{}{}'.format(site_t, url)
        image = get_img(url)
        if filename:
            show(filename.group(1))
            save_img(image, filename.group(1))
        else:
            show(url[-10])
            save_img(image, url[-10])
    return len(urls)


def main(download_many):
    t0 = time.time()
    count = download_many(urls)
    elapsed = time.time() - t0
    msg = '\n{} images downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many)
