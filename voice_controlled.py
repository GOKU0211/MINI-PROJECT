import speech_recognition as sr
import requests

# Replace this with the IP printed by ESP32 in Serial Monitor
ESP32_IP = "http://192.168.1.50"  # Example, update with real IP

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something (like 'light on' or 'light off')...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn’t understand.")
        return ""
    except sr.RequestError:
        print("Speech service error.")
        return ""

while True:
    cmd = listen_command()
    if "on" in cmd:
        requests.get(f"{ESP32_IP}/on")
        print("Light turned ON")
    elif "off" in cmd:
        requests.get(f"{ESP32_IP}/off")
        print("Light turned OFF")
