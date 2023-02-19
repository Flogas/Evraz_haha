import json
import random
import time
import kafka
from kafka import KafkaConsumer
import json
import pandas as pd


consumer = KafkaConsumer(
    auto_offset_reset = "earliest",
    enable_auto_commit = True,
    bootstrap_servers='rc1a-2ar1hqnl386tvq7k.mdb.yandexcloud.net:9091',
    sasl_mechanism='SCRAM-SHA-512',
    security_protocol='SASL_SSL',
    sasl_plain_username='9433_reader',
    sasl_plain_password='eUIpgWu0PWTJaTrjhjQD3.hoyhntiK',
    ssl_cafile = "C:/Users/User/.kafka/CA.pem",
    group_id='$Датамыши',


)
consumer.subscribe(['zsmk-9433-dev-01'])

consumer.poll()
#go to end of the stream
consumer.seek_to_beginning()
#start iterate
df = pd.DataFrame([''],[''])
for message in consumer:
    msg = message.value
    msg_json = json.loads(msg.decode('utf-8'))
    print(msg_json.items())
    data = pd.DataFrame(msg_json.items())
    df = pd.concat([df, data])
    df.to_csv("exgauster_data_3_weeks.csv")

consumer.close()