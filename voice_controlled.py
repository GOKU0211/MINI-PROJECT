# Modified voice_controlled.py

import speech_recognition as sr
# import requests # REMOVED: No longer using Wi-Fi (HTTP) communication

# ESP32_IP = "http://192.168.1.50"  # REMOVED: No longer needed for Serial

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
        log(" Listening for command...")
        # Add a pause to adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        log(f"You said: {command}")
        
        # --- REMOVED: Wi-Fi (HTTP) sending logic ---
        # if "on" in command:
        #     requests.get(f"{ESP32_IP}/on")
        #     log(" Light turned ON")
        # elif "off" in command:
        #     requests.get(f"{ESP32_IP}/off")
        #     log(" Light turned OFF")
        # else:
        #     log(" Command not recognized")
        # ---
        
        return command # We return the command string to Interface.py for processing
    except sr.UnknownValueError:
        log(" Sorry, I didn’t understand.")
        return ""
    except sr.RequestError:
        log(" Speech service error.")
        return ""

def record_sample(filename="temp.wav", duration=3):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Recording... Speak now")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=duration)
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    return filename

# The rest of the file remains the same.