import json
from time import sleep
from uuid import uuid4

from bs4 import BeautifulSoup
from kafka import KafkaProducer
import requests

def fetch_raw(recipe_url):
    html = None
    print('Processing..{}'.format(recipe_url))
    try:
        r = requests.get(recipe_url, headers=headers)
        if r.status_code == 200:
            html = r.text
    except Exception as ex:
        print('Exception while accessing raw html')
        print(str(ex))
    finally:
        return html.strip()


def get_recipes():
    recipies = []
    salad_url = 'https://www.allrecipes.com/recipes/96/salad/'
    url = 'https://www.allrecipes.com/recipes/96/salad/'
    print('Accessing list')

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            links = soup.select('.fixed-recipe-card__h3 a')
            idx = 0
            for link in links:

                sleep(2)
                recipe = fetch_raw(link['href'])
                recipies.append(recipe)
                idx += 1
                if idx > 2:
                    break
    except Exception as ex:
        print('Exception in get_recipes')
        print(str(ex))
    finally:
        return recipies


def publish_message(producer_instance, topic_name, key, value, partition):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        # Successful result returns assigned partition and offset
        response_from_kafka = producer_instance.send(topic_name, key=key_bytes, value=value_bytes, partition=partition)
        metadata = response_from_kafka.get(timeout=10)
        print('published to')
        print (metadata.topic)
        print('with offset')
        print (metadata.offset)
        # block until all async messages are sent
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
    kafka_producer = connect_kafka_producer()
    while True:
        # all_recipes = get_recipes()
        uuid = uuid4()
        publish_message(kafka_producer, 'testing', 'raw', str(uuid) + "partition 2", 0)
        publish_message(kafka_producer, 'testing', 'raw', str(uuid) + "partition 2", 1)
        print(uuid)
        sleep(2)
            # if kafka_producer is not None:
            #     kafka_producer.close()