import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def talk(text):
    engine.say("Hi")
    engine.say(text)
    engine.runAndWait()
def take_input():
    try:
        with sr.Microphone() as source:
            print("Listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

    except:
        pass
    return command

def run():
    command = take_input()
    talk(command)
    if "play" in command:
        song = command.replace("play"," ")
        pywhatkit.playonyt("playing"+song)
        print(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M:%p")
        talk("Current time is"+ time)

run()