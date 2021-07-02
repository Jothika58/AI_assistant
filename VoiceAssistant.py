import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyjokes

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #voicechager if 0, male; if 1, female
newVoiceRate = 190 #voice rate
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello! This is Jo's AI class")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishname():
    speak("Welcome back madam!")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <=12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good afternoon")
    elif hour >=18 and hour <=24:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Fresher's Community at your service. How can I help you?")

wishname()

def takecmd():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, 'en=US')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please....")

        return "None"
    return query

def sendmail(to, content): #put your gmail in low secure mode in settings
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","yourpassword")
    server.sendmail("text@gmail.com", to, content)
    server.close()
def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishname()

    while True:
        query = takecmd().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentence=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takecmd()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in google chrome" in query:
            speak("What should I search?")
            chromepath = "type the chrome path in your system %s"
            search = takecmd().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "play songs" in query:
            songs_dir = "path of the song"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should I remember?")
            data = takecmd()
            speak("You said me to remember" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you remember that"+ remember.read())
        elif "joke" in query:
            jokes()






