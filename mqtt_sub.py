import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "192.168.31.33"  # Replace with the IP address of your Raspberry Pi
broker_port = 1883
topic = "test"

# Define the callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe(topic)
    else:
        print("Connection failed with code", rc)

# Define the callback for receiving messages
def on_message(client, userdata, message):
    print(f"Received message: {str(message.payload.decode())} on topic: {message.topic}")

# Create a new MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the loop to process callbacks and reconnect if needed
client.loop_forever()
