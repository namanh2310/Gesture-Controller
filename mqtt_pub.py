import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "192.168.31.33"  # Replace with the IP address of your Raspberry Pi
broker_port = 1883
topic = "test"

# Create a new MQTT client instance
client = mqtt.Client()

# Define the callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed with code", rc)

client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Publish a message
message = "Hello from Raspberry Pi"
client.loop_start()
client.publish(topic, message)
print(f"Published message: {message} to topic: {topic}")
client.loop_stop()

# Disconnect from the broker
client.disconnect()
