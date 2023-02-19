import json
import random
import time

import kafka
from kafka import KafkaConsumer
import json
import pandas as pd


consumer = KafkaConsumer(
    bootstrap_servers='rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091',
    sasl_mechanism='SCRAM-SHA-512',
    security_protocol='SASL_SSL',
    sasl_plain_username='9433_reader',
    sasl_plain_password='eUIpgWu0PWTJaTrjhjQD3.hoyhntiK',
    ssl_cafile = "C:/Users/User/.kafka/CA.pem",
    group_id='$Датамыши',

)
consumer.subscribe(['zsmk-9433-dev-01'])

for message in consumer:
    msg = message.value
    msg_json = json.loads(msg.decode('utf-8'))
    print(type(msg_json))
    print(msg_json.items())
    z = pd.DataFrame(msg_json.items())
    z.to_csv("exgauster.csv")


# unsubscribe and close  consumer
consumer.unsubscribe()
consumer.close()