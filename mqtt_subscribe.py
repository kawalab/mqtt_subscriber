#MQTT library
import paho.mqtt.client as mqtt
#json data library
import json
#datetime library
import datetime
#data　analysis library
#import pandas as pd
#import os

#SenseWay Mission Connect userID
USER_ID = None
#SenseWay Mission Connect passward : warning!!
USER_PASS = None
#LoRa dev ID
DEVEUI = None

"""MQTT receive data!!"""
receive_data = None
receive_time = None
receive_diveui = None
receive_count = None


""" 
not complete
def csv_data_write():
  df = pd.DataFrame(datalist, colums = ["EUI", "data", "time", "count"])

  df.to_csv(os.getcwd(),encoding="utf-8")

# receive date time is UTC... need UTC to JST time. this function UTC string to JST string changing!
# https://dev.classmethod.jp/server-side/python/python-time-string-timezone/
def utc_to_jst(timestamp_utc):
    datetime_utc = datetime.datetime.strptime(timestamp_utc)
    datetime_jst = datetime_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    timestamp_jst = datetime.datetime.strftime(datetime_jst, '%Y-%m-%d %H:%M:%S.%f')
    return timestamp_jst
"""

# connect MQTT broker callback
def on_connect(client, userdata, flag, rc):
  print("Connected with result code : " + str(rc))
  #print("user ID : " + USER_ID + ", dev ID :" + DEVEUI)
  client.subscribe("lora/" + USER_ID + "/" + DEVEUI + "/rx")

# disconnect MQTT broker callback
def on_disconnect(client, userdata, flag, rc):
  if  rc != 0:
    print("Unexpected disconnection.\n")

# message receive callback
def on_message(client, userdata, msg):
  # msg.topic -> topic ，msg.payload -> main message
  print("Received message '" + str(msg.payload))
  json_data = json.loads(msg.payload)

  # token
  print("===================receive data token===================")
  # temp data hex to Dec, / 100
  receive_data = float(int(json_data["mod"]["data"], 16) / 100)
  print("receive data : " + str(receive_data))
  # gateway receive time
  receive_time = (str(json_data["gw"][0]["date"]))
  print("receive time : " + receive_time)
  # dev id
  receive_diveui = json_data["mod"]["devEUI"]
  print("receive EUI  : " + receive_diveui)
  # dev send count
  receive_count = json_data["mod"]["cnt"]
  print("send count   : " + str(receive_count))
  print("========================================================")
  #csv_data_write()

# MQTT connect opition
client = mqtt.Client()
#connect callback setting
client.on_connect = on_connect
#disconnect callback setting
client.on_disconnect = on_disconnect
#message callback setting
client.on_message = on_message
#client userid pass set
client.username_pw_set(USER_ID, USER_PASS)
#client connect execute! connect to sensewaymission connect
client.connect("mqtt.senseway.net", 1883, 600)

client.loop_forever()