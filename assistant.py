import datetime
import os
from random import randint
import webbrowser
import smtplib

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Sir Rashid's assistant. Please tell how may I help you?")


def takeCommand():
    # will take input as voice and returns string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 800  # increase to make it listen higher levels of volumes.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("Could you say that again please?")
        return "None"
    return query

# this method needs your google account to be enable less secured apps!!!
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "passwordhere")
    server.login("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        
        elif 'name' in query:
            speak("My name is David")
            print("My name is David")
        
        elif 'about your developer' in query:
            speak("This virtual assistant is coded by rashid")    

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'me a song' in query:
            music_dir = "E:\\ForSDcard"
            songs = os.listdir(music_dir)
            print("songs")
            rand = randint(0, 2)
            os.startfile(os.path.join(music_dir, songs[rand]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Rashid\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        elif 'exit' in query or 'quit' in query or 'close' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 16:
                speak("Have a nice day!")

            elif hour >= 16 and hour < 18:
                speak("Good Evening!")

            else:
                speak("take care sir, Good night!")
                print("take care sir, Good night!")
            exit()
        
        elif 'say that' in query or 'say' in query:
            query.replace("say", "", 1)    
            query.replace("that", "", 1)
            speak(query)    

        elif 'email to rashid' in query:
            try:
                ("What should I say?")
                content = takeCommand()
                to = "rashidwassan78611011@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Unable to send this Email...")    
                