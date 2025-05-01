import speech_recognition 
import pyttsx3
from translate import Translator

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def trans1():
    string=str(input("Enter your string: "))
    conlan=str(input("In which language you have to translate: "))
    translator= Translator(from_lang="english",to_lang=conlan)
    translation = translator.translate(string)
    speak("Sure sir")
    print(translation)