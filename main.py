from clearblade.ClearBladeCore import System, Query
import psutil  # for getting system info
import time

SystemKey = "f2a493ca0b82d7998df8f4f9ad47"
SystemSecret = "F2A493CA0B94ECA9ADCD9ABAF98801"

mySystem = System(SystemKey, SystemSecret)

bobby = mySystem.User("rickybobby@gmail.com", "iynfyl")

mqtt = mySystem.Messaging(bobby)
code = mySystem.Service("StoreMessageService")


def on_connect(client, userdata, flags, rc):
    for x in range(25):
        client.publish("cpuTopic", psutil.cpu_percent())
        time.sleep(.5)
        code.execute(bobby, {})
        time.sleep(.5)


mqtt.on_connect = on_connect
mqtt.connect()
time.sleep(30)
mqtt.disconnect()
