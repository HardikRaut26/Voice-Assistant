import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime
import pyautogui
from dotenv import load_dotenv

load_dotenv()

WHATSAPP_CONTACT_1 = os.getenv("WHATSAPP_CONTACT_1")

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

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
                   Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enter the message- "))
        time_hour = int(datetime.now().strftime("%H"))
        time_min = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))
        pywhatkit.sendwhatmsg(WHATSAPP_CONTACT_1, message, time_hour=time_hour, time_min=time_min)
    elif a == 2:
        pass

