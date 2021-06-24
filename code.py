import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import time
from datetime import date
from datetime import datetime as dt
import os
import random
import playsound
import smtplib
import requests
from pprint import pprint
import json
import pyowm

# Creating an engine to get and set the prpority of voices.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    # speak function will return the user input(through microphone/speaker/mic) in the form of string output
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()  # recognizer class will recognize the audio from thr user
    with sr.Microphone() as source:
        # this will listen users audio through system microphone as source
        print("Listening...")  # Listening to the user
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")

    elif hour >= 16 and hour < 20:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("Hello, I am Tango your personal assistant. Please tell me how may I help you")


def weather_data(temp):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                       temp+'&APPID=f4f6320f7e83c12a0b7db13a5e84af67&units=metric')
    return res.json()


def print_weather(result, city):
    print("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    speak("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    speak("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    speak("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    speak("Weather: {}".format(result['weather'][0]['main']))


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("yourEmail@gmail.com", "Your Password") # you have to provide you email and password for login 
    server.sendmail("yourEmail@gmail.com", to, content)  
    server.close()

def reminder_music():
    music = ["Best Reminder.mp3", "Reminder.mp3"]
    try:
        playsound.playsound(random.choice(music))
    except Exception as e:
        print(e)
    
def alarm_music():
    music = ["car_horn_alarm.mp3", "morning_alarm.mp3"]
    try:
        playsound.playsound(random.choice(music))
    except Exception as e:
        print(e)


dict = {'vishal': '18BCS3503@cuchd.in',
        'hemant': '18BCS3518@cuchd.in', 'ankit': '18BCS3508@cuchd.in',
        'silajitdas': '18BCS3532@cuchd.in'
        }


if __name__ == "__main__":
    wishMe()

    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open github' in query:
            webbrowser.open("https://github.com/")

        elif 'open linkedin' in query:
            webbrowser.open("https://in.linkedin.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open gmail' in query:
            webbrowser.open("http://gmail.com/")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            a = random.choice(songs)
            print(a)
            os.startfile(os.path.join(music_dir, a))

        elif 'how are you' in query:
            li = ['good', 'fine', 'great', 'awesome']
            response = random.choice(li)
            speak(f"I am {response}")

        elif 'who are you' in query:
            speak("I am your personal assistant and my name is Tango")

        elif 'what can you do' in query:
            li_commands = {
                "open websites": "Example: 'open youtube.com'",
                "time": "Example: 'what time it is?'",
                "date": "Example: 'what date it is?'",
                "launch applications": "Example: 'launch chrome'",
                "tell me": "Example: 'tell me about India'",
                "weather": "Example: 'what weather/temperature in Mumbai?'",
                "news": "Example: 'news for today' ",
            }
            ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
                    I can open websites for you, launch application and more. See the list of commands-"""
            print(ans)
            pprint.pprint(li_commands)
            speak(ans)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "what is the today's date" in query:
            current_date = datetime.datetime.today().strftime('%d-%b-%Y')
            print(f"Today's date is {current_date}")
            speak(f"Today's date is {current_date}")

        elif "what date was yesterday" in query:
            yesterday_date = datetime.datetime.today() - datetime.timedelta(days=1)
            yesterday_date_formatted = yesterday_date.strftime('%d-%b-%Y')
            print(f"yesteday date was {yesterday_date_formatted}")
            speak(f"yesteday date was {yesterday_date_formatted}")

        elif "what date was before yesterday" in query:
            before_yesterday_date = datetime.datetime.today() - datetime.timedelta(days=2)
            before_yesterday_date_formatted = before_yesterday_date.strftime(
                '%d-%b-%Y')
            print(
                f"before yesteday date was {before_yesterday_date_formatted}")
            speak(
                f"before yesteday date was {before_yesterday_date_formatted}")

        elif "what date will tomorrow" in query:
            tomorrow_date = datetime.datetime.today() + datetime.timedelta(days=1)
            tomorrow_date_formatted = tomorrow_date.strftime('%d-%b-%Y')
            print(f"tomorrow date will {tomorrow_date_formatted}")
            speak(f"tomorrow date will {tomorrow_date_formatted}")

        elif "what date will after tomorrow" in query:
            after_tomorrow_date = datetime.datetime.today() + datetime.timedelta(days=2)
            after_tomorrow_date_formatted = after_tomorrow_date.strftime('%d-%b-%Y')
            print(f"after tomorrow date will {after_tomorrow_date_formatted}")
            speak(f"after tomorrow date will {after_tomorrow_date_formatted}")

        elif "what is the day today" in query:
            now = datetime.datetime.now()
            # Use %A for the abbreviated full weekday name
            print(f"Today's day is {now.strftime('%A')}")
            speak(f"Today's day is {now.strftime('%A')}")

        elif "remind me" in query:
            speak("What shall I remind you about?")
            text = takecommand()
            speak("In how much time?")
            speak("Please provide your time in the form of integer or float type only")
            local_time = takecommand()
            time1 = float(local_time)
            time2 = timer1 * 60  # Python’s time.sleep() method requires seconds, not minutes. So I need to convert minutes to seconds.
            speak("Reminder has been set successfully!")
            speak(f"ok, I will remind you after {time2} seconds")
            time.sleep(time2)
            speak(f"It is a reminder for {text}") 
            reminder_music()
            
        elif "set the alarm" in query:
            speak("Welcome to the alarming interface")
            speak("Tell me the time sir to set the alarm !")
            speak("Please provide your time in the form of integer or float type only")
            set_alarm_timer = takecommand()
            timer = float(set_alarm_timer)
            timer1 = timer * 60
            speak("Alarm has been set successfully!")
            speak(f"you will be inform after {timer1} seconds")
            time.sleep(timer1)
            print("Time to Wake up")
            alarm_music()

        elif 'open chrome browser' in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'open Vscode' in query:
            path = "C:\\Users\\vishal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open vlc media player' in query:
            path = "C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"
            os.startfile(path)

        elif 'send email to' in query:
            try:
                name = list(query.split())  # extract receiver's name
                name = name[name.index('to')+1]
                speak("What should i say")
                content = takecommand()
                to = dict[name]  
                sendEmail(to, content)
                speak("Email has been sent")
                print("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry unable to send the email at the moment.Try again")

        elif "tell me today's weather" in query:
            speak("Tell me the city name of which you want the weather report !")
            city = takecommand()
            try:
                temp = 'q='+city
                w_data = weather_data(temp)
                print_weather(w_data, city)
                print()
            except:
                print('City name not found...')
                speak('City name not found...')

        elif 'quit' in query:
            exit()
