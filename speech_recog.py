import speech_recognition as sr
recogniser=sr.Recognizer()

def voice_capture():
    with sr.Microphone() as source:
        print("***LISTENING***")
        audio=recogniser.listen(source)
    return audio

def voice_to_text(audio):
    try:
        text=recogniser.recognize_google(audio)
        print("You said:\n"+text)
    except sr.UnknownValueError:
        text=""
        print("Sorry, i count get what you said")
    except sr.RequestError as e:
        text=""
        print("Error;{0}".format(e))
        return text
    
if __name__=="__main__":
    audio_data=voice_capture()
    voice_to_text(audio_data)