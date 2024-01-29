import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "YOUR_API_KEY :)"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(command):
    engine.say(command)
    engine.runAndWait()

def take_input():

        with sr.Microphone() as source:
            print("Listening......")
            recognizer = sr.Recognizer()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            recognizer.adjust_for_ambient_noise(source, duration=1)   
            command = command.lower()
            print("User: "+command)
        return command

def chatbot():
        command = take_input()
        
        chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=[{"role":"user","content":"Please Explain me it 2 lines"+command}])
        talk(chat.choices[0].message.content) 
        print("Bot: "+chat.choices[0].message.content)

chatbot()