import datetime
import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 120)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)

def speak(str):
    engine.say(str)
    engine.runAndWait()
    engine.stop()


def wishme():
    hours = datetime.datetime.now().hour
    mins = datetime.datetime.now().minute
    days = datetime.datetime.now().day
    months = str(datetime.datetime.now().date().month)
    months = datetime.datetime.strptime(months, '%m').strftime('%B')
    years = datetime.datetime.now().date().year
    if hours < 12:
        speak("good morning sir")
    elif 12 <= hours < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("today's date is "+str(days)+months+" "+str(years)+"and time is"+str(hours)+str(mins))
    speak("how may i help")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        speak("say that again please...")
        take_command()
        return "None"
    return query


def sendmail(to):
    ob = smtplib.SMTP("smtp.gmail.com", port=587)

    ob.starttls()
    ob.login("coderxabhijeet007@gmail.com", "#CODERoo7")

    subject = "Testing python email"
    body = "Hello receiver,\n\nhow are you doing"

    message = "Subject:{}\n\n{}".format(subject, body)

    ob.sendmail("coderxabhijeet007", "006abhijeet600@gmail.com", message)
    ob.quit()



if __name__ == '__main__':
    # wishme()
    query = take_command().lower()
    if "open notepad" in query:
        speak("heading")
        note = take_command()
        if not os.path.exists("file.txt"):
            with open(os.path.join("file.txt"), 'w') as op:
                pass
                op.write(note)
        else:
            with open(os.path.join("file.txt"), 'w') as op:
                pass
                op.write(note)
        osCommandstring = "notepad.exe file.txt"
        os.system(osCommandstring)

    elif "wikipedia" in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak(f"according to wikipedia {results}")
        print(results)

    elif "youtube" in query:
        webbrowser.get('"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" %s').open("youtube.com", new=2)

    elif "mail to" in query:
        query = query.replace("send mail to ", "")
        try:
            sendmail(query)
            speak("email has been sent")
        except Exception as e:
            print(e)
            speak("sorry task failed")

    elif "search" in query:
        query = query.replace("search ", "")
        webbrowser.open(f"https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57.6203j0j9&sourceid=chrome&ie=UTF-8")

    elif "who are you" in query:
        speak("I am your desktop assistant")

    elif "open code" in query:
        os.startfile("C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif "play music" in query:
        os.startfile("C:\\Users\\lenovo\\Music\\Satisfya - Imran Khan Trending Tiktok song colour coded.mp3")