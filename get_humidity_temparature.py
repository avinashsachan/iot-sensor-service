import os
import time
from datetime import datetime
import sys
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import json
import requests
import uuid
import re

mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])



def LogData(logdate,humidity,temparature):

	# defining the api-endpoint
	API_ENDPOINT = "https://dataloggerserver.tk/logdata.php"

	# data to be sent to api

	header = {"Content-type": "application/json"}
	data = {"key":"(cRos+y1lxa2" , 
		"logdate" : logdate,
		"humidity" : humidity ,
		"temparature": temparature,
		"mac" : mac }

	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, json = data , headers=header)

	# extracting response text
	pastebin_url = r.text
	#print("The pastebin URL is:%s"%pastebin_url)


while True:
	try:
		dt =  datetime.now()
		humidity,temperature = dht.read_retry(dht.DHT11, 4)
		humidity = round(humidity, 2)
		temperature = round(temperature, 2)
		#print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))

		#with open("/tmp/hum.log","a") as f:
		#	f.write(u"Date: {},Temperature: {:g}, Humidity: {:g}%\n".format(dt.strftime("%y-%m-%d %H:%M:%S"),temperature, humidity))
		LogData(dt.strftime("%y-%m-%d %H:%M:%S"),humidity,temperature)
	except:
		#time.sleep(30)
		#None
		print(sys.exc_info()[1])
	time.sleep(600)
	#sys.exit(1)

