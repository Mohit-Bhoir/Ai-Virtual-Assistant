import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import requests
import pywhatkit
from bs4 import BeautifulSoup



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail.gmail.com','your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
         speak("Good Morning !")

    elif hour>= 12 and hour <18:
        speak("Good afternoon !")

    else:
        speak("Good Evening !")

    speak("I am Jarvis . Sir please tell me how can I help you ")
    
    

def takeCommand():
    #It takes microphone input from the function and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
        
        

    try : 
       print("Recognizing...") 
       query = r.recognize_google(audio,language='en-in')
       print(f"User said : {query}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query


if __name__=="__main__":
    WishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'who is 'in query:
            speak("searching")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            print(results)
            speak(results)

        if 'what is 'in query:
            speak("searching")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            print(results)
            speak(results)


        #Logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak('I am fine Sir , what about you ?')

        elif 'you need to take a break' in query:
            speak('Ok sir , you can call me any time !')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'search youtube' in query:
            speak("Ok sir , this is what I found for your search")
            query.replace("jarvis","")
            query.replace("search youtube","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir !")
            
        elif 'open google' in query:
            webbrowser.open("google.com")   
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")  
            
        elif 'open javaTpoint' in query:
            webbrowser.open("javaTpoint.com")  
            

        elif 'play music' in query :
            music_dir = "C:\\english"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
            speak("I hope you are using your time wisely")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\mangesh\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'send email to mohit' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "mohityourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir I am unable to send Email at this moment ")

        elif 'temperature in thane' in query:
             search = "temperature in  thane"
             url = f"https://www.google.com/search?q={search}"
             r = requests.get(url)
             data = BeautifulSoup(r.text,"html.parser")
             temp = data.find("div",class_="BNeawe").text
             print(f"current {search} is {temp}")
             speak(f"current {search} is {temp}")