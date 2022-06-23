from decimal import Decimal
import RPi.GPIO as GPIO
#import PCF8591 as ADC
import math
import requests
import time
#import LCD1602 as LCD
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import json

def movement(self, params, packet):
    print ('Recieved msg from core')
    print ('Topic: '+ packet.topic)
    print("Payload: ", (packet.payload))






GPIO.setmode(GPIO.BOARD)
myMQTTClient = AWSIoTMQTTClient("JasikaAbadir") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a216tat0r5zfcf-ats.iot.eu-west-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi/certs/Amazon-root-CA-1.pem", "/home/pi/certs/private.pem.key", "/home/pi/certs/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()
#myMQTTClient.subscribe("car/move", 1, movement)

#while True:
#    time.sleep(5)

print("sending payload to aws..")
myMQTTClient.publish(
        topic="car/move",
        QoS=1,
        payload= '{"hey": 2}')
