import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import os
import webbrowser
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

author = 'AMC'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your gmail address', 'your password')
    server.sendmail('your gmail address', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")

    speak("How may i help you?")


def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . . ")
        recog.pause_threshold = 2
        audio = recog.listen(source)
    try:
        print("Recognizing . . .")
        query = recog.recognize_google(audio, language='en-in')
        print(f"User said : {query} \n")
    except Exception as e:
        speak(f"Sorry {author}, there has been an {e}")

    return query


# speak(f"Welcome {author}, I am JARVIS")
# wishMe()
# takeCommand()
if 1:
    query = takeCommand()
    if 'wikipedia' and 'who' in query:
        speak("Searching WIKIPEDIA . . .")
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wiki")
        speak(results)
    elif 'news' in query:
        speak("News Update ...")
        query = query.replace("news", "")
        url = "enter your news url"
        news = json.loads(requests.get(url).text)
        articles = news['articles']
        for article in articles:
            print(article['author'])
            speak(article['author'])
            print(article['title'])
            speak(article['title'])
            print(article['description'])
            speak(article['description'])
            speak("Moving on, we have an article by")

    elif 'open google' in query:
        url = "http://www.google.com/"
        webbrowser.open(url)

    elif 'open youtube' in query:
        url = "http://www.youtube.com/"
        webbrowser.open(url)

    elif 'search browser' in query:
        speak("What should i search for?")
        userQuery = takeCommand().lower()
        webbrowser.open(f"{userQuery}")

    elif 'ip address' in query:
        ip = requests.get("http://api.ipify.org/").text
        print(f"your IP is {ip}")
        speak(f"Your IP is {ip}")

    elif 'open command prompt' in query:
        os.system("start cmd /K echo Hello, this is your command prompt.")

    elif 'play music' in query:
        music_dir = 'D:\\jarvis\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'play youtube' in query:
        speak("What should i search in youtube ?")
        cm = takeCommand().lower()
        kit.playonyt(f"{cm}")

    elif 'send message' in query:
        speak("Who do you want to send the message ?")
        num = input("Enter number: \n")
        speak("what do you want to send?")
        msg = takeCommand().lower()
        speak("Please Enter Time sir.")
        H = int(input("Enter hour ?\n"))
        M = int(input("Enter Minutes ?\n"))
        kit.sendwhatmsg(num, msg, H, M)

    elif 'send email' in query:
        speak("What should i send sir ?")
        content = takeCommand().lower()
        speak("Whom to send the email, enter email address sir")
        to = input("Enter Email Address: \n")
        sendMail(to, content)
