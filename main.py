from clearblade.ClearBladeCore import System, Query
import psutil  # for getting system info
import time
import json

SystemKey = "f2a493ca0b82d7998df8f4f9ad47"
SystemSecret = "F2A493CA0B94ECA9ADCD9ABAF98801"

mySystem = System(SystemKey, SystemSecret)

bobby = mySystem.User("rickybobby@gmail.com", "iynfyl")

mqtt = mySystem.Messaging(bobby)
code = mySystem.Service("StoreMessageService")

# for x in range(10):
#     print(psutil.cpu_percent())
#     time.sleep(.5)
#     # code.execute(bobby, {})
#     time.sleep(.5)


def on_connect(client, userdata, flags, rc):
    for x in range(10):
        pct = psutil.cpu_percent()
        timeStamp = time.time()
        blob = {
            "pct":
            pct,
            "timestamp": str(timeStamp)
        }
        print("publishing blob: " + json.dumps(blob))
        client.publish("cpuTopic", json.dumps(blob))
        time.sleep(1)


mqtt.on_connect = on_connect
mqtt.connect()
time.sleep(12)
mqtt.disconnect()
