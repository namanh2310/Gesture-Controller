import speech_recognition as sr
import pyaudio

p = pyaudio.PyAudio()
r = sr.Recognizer()
mic = sr.Microphone()

print("Start talking!")

for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i).get('name'))

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)