import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyautogui
import os
import pyjokes
from PyDictionary import PyDictionary as diction
import smtplib
import requests
import pywhatkit
import keyboard
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail.gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("   ")


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon !")

    else:
        speak("Good Evening !")

    speak("My name is Jarvis. A virtual AI assistant")
    speak("Please tell me how can I help you")



def takeCommand():
    # It takes microphone input from the function and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query


def YoutubeAuto():
    speak('Whats your command ? ')
    comm = takeCommand()

    if 'pause' in comm:
        keyboard.press('k')

    elif 'restart' in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'fullscreen' in comm:
        keyboard.press('f')

    elif 'film mode' in comm:
        keyboard.press('t')

    speak('Done sir !')

def ChromeAuto():
    speak("Chrome Automation Started !")
    command = takeCommand()

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'history' in command:
        keyboard.press_and_release('ctrl + h')

    elif 'downloads' in command:
        keyboard.press_and_release('ctrl + j')

def Dict():
    speak("Activating Dictionary...")
    speak("What is the problem")
    problem = takeCommand()

    if 'meaning' in problem:
         problem = problem.replace("what is the", "")
         problem = problem.replace("jarvis", "")
         problem = problem.replace("of", "")
         problem = problem.replace("meaning", "")
         result = diction.meaning(problem)
         print(result)
         speak(result)

    elif 'synonym' in problem:
        problem = problem.replace("what is the", "")
        problem = problem.replace("jarvis", "")
        problem = problem.replace("of", "")
        problem = problem.replace("synonym", "")
        result = diction.synonym(problem)
        print(result)
        speak(result)

    elif 'antonym' in problem:
        problem = problem.replace("what is the", "")
        problem = problem.replace("jarvis", "")
        problem = problem.replace("of", "")
        problem = problem.replace("antonym", "")
        result = diction.antonym(problem)
        print(result)
        speak(result)

def news():
    main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=API_KEY'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth",]
    for ar in articles:
        head.append(ar["title"])

    for i in range(len(day)):
        speak(f"Todays'{day[i]} news is :{head[i]}")

def starter():
     WishMe()
     while True:
        # if 1:
        query = takeCommand().lower()

        if 'who is ' in query:
            speak("searching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)

        if 'what is ' in query:
            speak("searching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak('I am fine Sir , what about you ?')

        elif 'you need to take a break' in query:
            speak('Ok sir , you can call me any time !')

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'close youtube' in query:
            os.system('TASKKILL /F /im chrome.exe ')

        elif 'search youtube' in query:
            speak("Tell me what to search !")
            search = takeCommand()
            speak("Ok sir , this is what I found for your search")
            web = 'https://www.youtube.com/results?search_query=' + search
            webbrowser.open(web)
            speak("Done sir !")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'close google' in query:
            os.system('TASKKILL /F /im chrome.exe ')

        elif 'Google search' in query:
            speak("Ok sir , this is what I found for your search")
            query.replace("jarvis", "")
            query.replace("search google", "")
            pywhatkit.search(query)
            speak("Done sir !")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'close stack overflow' in query:
            os.system('TASKKILL /F /im chrome.exe ')

        elif 'open javaTpoint' in query:
            webbrowser.open("javaTpoint.com")

        elif 'close javaTpoint' in query:
            os.system('TASKKILL /F /im chrome.exe ')

        elif 'open maps' in query:
            webbrowser.open('https://www.google.com/maps')

        elif 'close maps' in query:
            os.system('TASKKILL /F /im chrome.exe ')

        elif 'play music' in query:
            music_dir = "C:\\english"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, 
            
            ))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
            speak("I hope you are using your time wisely")
            print(f"Sir , the time is {strTime}")
            print("I hope you are using your time wisely")

        elif 'open vs code' in query:
            os.startfile('C:\\Microsoft VS Code\\_\\Code.exe')

        elif 'close vs code' in query:
            os.system('TASKKILL /F /im code.exe ')

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
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")

        elif 'screenshot' in query:
            speak("Ok sir , what should i name the file ?")
            path = takeCommand()
            path1name = path + ".png"
            path1 = "C:\\Screenshots\\"+path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile('C:\\Screenshots')
            speak("Here is your file sir !")

        elif 'pause' in query:
            keyboard.press('k')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'fullscreen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'downloads' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'Chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
            print(get)

        elif 'repeat my words' in query:
            jj = takeCommand()
            speak(f"you said : {jj}")

        elif 'my location' in query:
            speak('Ok sir , Wait a second')
            webbrowser.open('https://www.google.com/maps')

        elif 'meaning' in query:
            query = query.replace("what is the", "")
            query = query.replace("jarvis", "")
            query = query.replace("of", "")
            query = query.replace("meaning", "")
            result = diction.meaning(query)
            print(result)
            speak(result)

        elif 'synonym' in query:
            query = query.replace("what is the", "")
            query = query.replace("jarvis", "")
            query = query.replace("of", "")
            query = query.replace("synonym", "")
            result = diction.synonym(query)
            print(result)
            speak(result)

        elif 'antonym' in query:
            query = query.replace("what is the", "")
            query = query.replace("jarvis", "")
            query = query.replace("of", "")
            query = query.replace("antonym", "")
            result = diction.antonym(query)
            print(result)
            speak(result)

        elif 'dictionary' in query:
            Dict()

        elif "Tell me news" in query:
            speak("Please wait sir , fetching the latest news")
            news()

        elif "shut down" in query:
            os.system("shutdown/s/t 5")
            
        elif "restart" in query:
            os.system("shutdown/r/t 5")

        elif "sleep the sysytem" in query:
            os.system("roundll32.exe powrprof.dll,sesuspendstate 0,1,0")

        elif "ip address"  in query:
             ip = get("https://api.ipify.org").text
             speak(f"YOUR IP ADDRESS is {ip}")

        

        elif "open cmd" in query:
             os.system("start cmd")

if __name__ == "__main__":
                
         starter()

        