import paho.mqtt.client as mqtt
import json
import sqlite3
from django.conf import settings
from django.utils import timezone
import random
import time
import os
from django.apps import apps


conf = {
    'INSTALLED_APPS': [
        'app1'
    ],
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join('.', 'db.sqlite3'),
        }
    }
}

settings.configure(**conf)
apps.populate(settings.INSTALLED_APPS)


from app1.models import zbbtn, zbdoor, zbbtn


def on_connect(client, userdata, rc, properties=None):

    client.subscribe("zigbee2mqtt/+")
    #from .models import zbbtn, zbdoor, zbtmphum
          
def on_message(client, userdata, msg):
    
    pload = ""
    print ("msg.topic", msg.topic)
    if msg.topic == "zigbee2mqtt/zbdoor_1" or msg.topic == "zigbee2mqtt/zbdoor_2":
        pload = json.loads(msg.payload.decode('utf-8'))
        t = zbdoor(topic =str(msg.topic) , created_date = timezone.now(), battery = int(pload['battery']), 
            battery_low  = bool(pload['battery_low']), contact  = bool(pload['contact']), linkquality = int(pload['linkquality']), voltage = int(pload['voltage'])) 
        t.save()

    if msg.topic == "zigbee2mqtt/zbbtn_1":

        try:
            pload = json.loads(msg.payload.decode('utf-8'))
        
            if str(pload['action']):
                act = str(pload['action'])
                t1 = zbbtn(topic =str(msg.topic) , created_date = timezone.now(), battery = int(pload['battery']), 
                action  = act, linkquality = int(pload['linkquality']), voltage = int(pload['voltage'])) 
                print("t1 save")
                t1.save()           
                if act == "single":
                    publish(client, "1")
                if act == "double":
                    publish(client, "0")
        except:
            pass



    if msg.topic == "zigbee2mqtt/zbtemp_1":
        pload = json.loads(msg.payload.decode('utf-8'))
        t2 = zbtmphum(topic =str(msg.topic) , created_date = timezone.now(), battery = int(pload['battery']), 
            humidity  = float(pload['humidity']), temperature  = float(pload['temperature']), linkquality = int(pload['linkquality']), voltage = int(pload['voltage'])) 
        t2.save()
        
    
    print(client_id, "pload: ", pload)




def publish(client, action):
    topic = "sonoff1"
    result = client.publish(topic, action)
    print("publish")


client = mqtt.Client()
client_id = f'python-mqtt-{random.randint(0, 1000)}'

print("client --> " , client_id)

client.connect("192.168.1.141", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()



