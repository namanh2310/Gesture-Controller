import speech_recognition as sr
import pyaudio
import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "192.168.31.33"  # Replace with the IP address of your Raspberry Pi
broker_port = 1883
topic = "test"

p = pyaudio.PyAudio()
r = sr.Recognizer()
mic = sr.Microphone()

print("Start talking!")

for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i).get('name'))

# Create a new MQTT client instance
client = mqtt.Client()

# Define the callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed with code", rc)

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)

    client.on_connect = on_connect

    # Connect to the MQTT broker
    client.connect(broker_address, broker_port, 60)

    # Publish a message
    message = words
    client.loop_start()
    client.publish(topic, message)
    print(f"Published message: {message} to topic: {topic}")
    client.loop_stop()

    # Disconnect from the broker
    client.disconnect()
