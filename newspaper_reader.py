import pyttsx3
import requests
import json
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


url = input("Enter the API url with the API KEY from NewsAPI")

news = requests.get(url).text
news = json.loads(news)
articles = news['articles']
for article in articles:
    print(article['author'])
    speak(article['author'])
    print(article['title'])
    speak(article['title'])
    print(article['description'])
    speak(article['description'])
    speak("Moving on, we have an article by")
