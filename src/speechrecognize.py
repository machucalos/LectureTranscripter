import speech_recognition as sr 

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording")
        audio = r.listen(source)
    #use google for transcription
    print("Done")
    try:
        audio_text = r.recognize_google(audio)
        print(audio_text)
    except:
        print("Error decoding audio")


if __name__ == "__main__":
    record()
