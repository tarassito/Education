import json
from time import sleep

from kafka import KafkaConsumer
from kafka import TopicPartition

if __name__ == '__main__':
    parsed_topic_name = 'testing'
    # Notify if a recipe has more than 200 calories
    # calories_threshold = 200

    consumer = KafkaConsumer(auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], consumer_timeout_ms=1000)
    consumer.assign([TopicPartition(parsed_topic_name, 0)])
    while True:
        
        for msg in consumer:
            record = msg.value.decode('utf-8')
            print(record)
            sleep(8)

    # if consumer is not None:
    #     consumer.close()