import paho.mqtt.client as mqtt
from .config import MQTT_BROKER_URL, MQTT_BROKER_PORT

class MQTTClient:

    def __init__(self, broker_url, broker_port):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker_url, broker_port, 60)

    def start(self):
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe("printer/status")

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        # Update your data store with the message payload.
        # This may be a database, a file, or an in-memory store.
        # Depending on your needs, this might trigger additional actions or notifications.

mqtt_client_instance = MQTTClient(MQTT_BROKER_URL, MQTT_BROKER_PORT)
mqtt_client_instance.start()
