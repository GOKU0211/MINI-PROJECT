import speech_recognition as sr
recogniser=sr.Recognizer()

def voice_capture():
    with sr.Microphone as source:
        print("***LISTENING***")
        audio=recogniser.listen(source)
    return audio

def voice_to_text(audio):
    try:
        text=recogniser.recognize_google(audio)
        print("You said"+text)
    except sr.UnknownValueError:
        text=""
        print("Sorry, i count get what you said")
        