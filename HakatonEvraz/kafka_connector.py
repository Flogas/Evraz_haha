import json
import random
import time
import re
from kafka import KafkaConsumer
import json
from datamanager.models import Exhauster as ExhausterModel
from core.models import Exhauster as ExhausterData

consumer = KafkaConsumer(
    bootstrap_servers='rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091',
    sasl_mechanism='SCRAM-SHA-512',
    security_protocol='SASL_SSL',
    sasl_plain_username='9433_reader',
    sasl_plain_password='eUIpgWu0PWTJaTrjhjQD3.hoyhntiK',
    ssl_cafile=r"C:\Users\Вселенный\Desktop\HakatonEvraz\CA.pem",
    group_id='$Датамыши',
)

consumer.subscribe(['zsmk-9433-dev-01'])

pattern = r"\[.*\]"

for message in consumer:
    msg = message.value
    msg_json = json.loads(msg.decode('utf-8')) #.items()
    print(msg_json)
    for i in ExhausterModel.objects.all():
        print(i)
    # for key, value in msg_json:
    #     print(f'{key:>30} -> {value}')
    #     #print(*re.findall(pattern, key), "<-", value)


# unsubscribe and close  consumer
consumer.unsubscribe()
consumer.close()



