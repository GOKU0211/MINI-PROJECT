import speech_recognition as sr
import requests

ESP32_IP = "http://192.168.1.50"  # change to your ESP32 IP

# --- add this callback variable ---
update_callback = None  # this will be linked to GUI later


def log(message):
    """Send message to GUI if available, otherwise print."""
    if update_callback:
        update_callback(message)
    else:
        print(message)


def listen_once():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        log("🎤 Listening for command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        log(f"You said: {command}")

        if "on" in command:
            requests.get(f"{ESP32_IP}/on")
            log("💡 Light turned ON")
        elif "off" in command:
            requests.get(f"{ESP32_IP}/off")
            log("💤 Light turned OFF")
        else:
            log("🤔 Command not recognized")
        return command
    except sr.UnknownValueError:
        log("❌ Sorry, I didn’t understand.")
    except sr.RequestError:
        log("⚠️ Speech service error.")
