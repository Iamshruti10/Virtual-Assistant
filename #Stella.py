#modules 
import keyboard
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime

import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyautogui
import pyjokes
from pywikihow import search_wikihow
from playsound import playsound
import requests
from bs4 import BeautifulSoup
#from googletrans import Translator

#voice,engine:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishes:
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am stella, please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
    
def TaskExe():
    speak('hello,I am stella')
    speak("how may I help you")
     
#email:
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

#screenshot:
def screenshot():
    speak('ok, what should I name that file')
    path = takeCommand()
    path1name = path + ".png"
    path1 = "E:\\ScreenShots\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1name)
    os.startfile("E:\\ScreenShots\\")
    speak("done,your screenshot has been taken")

#Translator:
def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

#def Tran():
        #speak("Tell Me The Line!")
        #line = TakeHindi()
        #traslate = Translator()
        #result = traslate.translate(line)
        #Text = result.text
        #speak(Text)

#news:
def news():
    main_url ='http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey9f3e59f25c9e4eadb22f0d227093cc13'
 
    main_page = requests.get(main_url).json()
    articles = main_page('articles')
    head = []
    day=['first','second','third','forth','fifth','sixth','seventh','eight','ninth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range (len(day)):
     speak(f'todays {day[i]} news is {head[i]}')

#def WolfRamAlpha(query):
#    apikey = " TX5WE3-WHQRP32EK2"
 #   requester = wolframalpha.Client(apikey)
 #   requested = requester.query(query)

  #  try:
   #     answer = next(requested.results).text
    #    return answer
   # except:
    #    speak("The value is not answerable")

#def latestnews():
    #api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=#here paste your api key",
    #        "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=#here paste your api key",
     #       "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=#here paste your api key",
      #      "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=#here paste your api key",
       #     "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=#here paste your api key",
        #    "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=#here paste your api key"
#}

    #content = None
    #url = None
    #speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    #field = input("Type field news that you want: ")
    #for key ,value in api_dict.items():
       # if key.lower() in field.lower():
           # url = value
            #print(url)
            #print("url was found")
            #break
       # else:
           # url = True
#    if url is True:
#        print("url not found")

 #   news = requests.get(url).text
#    news = json.loads(news)
#    speak("Here is the first news.")

#   arts = news["articles"]
#    for articles in arts :
#        article = articles["title"]
#        print(article)
#        speak(article)
#        news_url = articles["url"]
#       print(f"for more info visit: {news_url}")
#
#       a = input("[press 1 to cont] and [press 2 to stop]")
#       if str(a) == "1":
#            pass
#        elif str(a) == "2":
#            break
        
#   speak("thats all")

#calculator:
#def Calc(query):
#    Term = str(query)
#   Term = Term.replace("stella","")
#    Term = Term.replace("multiply","*")
#    Term = Term.replace("plus","+")
#    Term = Term.replace("minus","-")
 #   Term = Term.replace("divide","/")
#
#  Final = str(Term)
 #   try:
 #       result = WolfRamAlpha(Final)
#        #print(f"{result}")
        #speak(result)

    #except:
         #speak("The value is not answerable")

#temperature:
def Temp():
        search = "temperature in satara"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} ")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of the Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            speak("no problem ")

#youtubeautomaton:
def YoutubeAuto():
        speak("Whats Your Command ?")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak("Done")

#chrome automation:
def ChromeAuto():
        speak("Chrome Automation started!")

        command = takeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

#Openapps:
def OpenApps():
    speak("ok,wait a second")

    if "code" in query:
       os.startfile("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code")
       
    elif "whatsapp" in query:
        os.startfile("C:\\Users\\ASUS\\Desktop\\whatsapp.exe")

    elif "intel IDEA" in query:
        os.startfile("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.2.2\\bin\\idea64.exe")
    
    elif "spotify" in query:
        os.startfile("C:\\Users\\ASUS\\Desktop\\Spotify.lnk")
    
    elif "microsoft word" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")

    elif "microsoft exel" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")
    
    elif "microsoft powerpoint" in query:
       os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")
       
    elif "zoom" in query:
        os.startfile("C:\\Users\\COMPUTER\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    
    elif "classroom" in query:
        os.startfile("https://classroom.google.com/u/0/h")

    elif 'chrome' in query:
            os.startfile("C:\\Users\\Public\\Desktop\\Brave.lnk")
    elif 'Youtube' in query:
           os.startfile('hhttps://www.youtube.com/')
    
    speak("your app has been started")

#closeapp:
def CloseApps():
    speak("ok,wait a second")

    if "code" in query:
       os.system("TASKKILL /F /im Code.exe")
       
    elif "whatsapp" in query:
            os.system("TASKKILL /F /im WhatsApp.exe")
       
    elif "intel IDEA" in query:
            os.system("TASKKILL /F /im idea64.exe")
    
    elif "spotify" in query:
            os.system("TASKKILL /F /im Spotify.exe")
       
    elif "microsoft word" in query:
            os.system("TASKKILL /F /im Microsoft Office Word 2007")
       
    elif "microsoft exel" in query:
            os.system("TASKKILL /F /im Microsoft Office Excel 2007")
       
    elif "microsoft powerpoint" in query:
      os.system("TASKKILL /F /im Microsoft Powerpoint 2007")
              
    elif "zoom" in query:
        os.system("TASKKILL /F /im Zoom.exe")
       
    elif 'youtube' in query:
        os.system("TASKKILL /F /in chrome.exe")
    
    elif 'google' in query:
        os.system("TASKKILL /F /in chrome.exe")

    speak("your app has been successfully closed")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
         speak("sure,wait a second")
         query = query.replace('stella',"")
         query = query.replace("searching youtube","")
         web = "https://www.youtube.com/results?search_query= " +query
         webbrowser.open(web)
         speak("done")    

        elif 'google' in query:
         speak("sure,wait a second")
         query = query.replace('stella',"")
         query = query.replace("searching google","")
         pywhatkit.search(query)
         speak("done")  

        elif 'website' in query:
            speak("sure,wait a second")
            query = query.replace('stella',"")
            query = query.replace("websiite","")
            web1 = query.replace('open',"")
            #web2 = 'https://www.' = web1 + '.com' 
            webbrowser.open(web1)
            speak('done')    

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
        
        elif'screenshot' in query:
            screenshot()
       
        elif 'joke' in query:
         speak(pyjokes.get_joke())
         print(speak)

        elif 'play' in query:
         song = query.replace('play', '')
         speak('playing ' + song)
         pywhatkit.playonyt(song)  

#repeat word
        elif'repeat my words' in query:
            speak("you'll go first")
            jj = takeCommand()
            speak(f'you said : {jj}')

#location
        elif "location" in query:
            speak("ok,wait a second")
            webbrowser.open('https://www.google.com/maps/place/')

#how to:
        elif 'how to' in query:
            speak("Getting data from internet!")
            op = query.replace("stella","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

#remember:
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("stella","")
            speak("you tell me remind you that :" +rememberMsg)
            remember = open('data.text','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:    
            remember = open('data.text','r')
            speak("you tell me that" + remember.read())

#open app:
        elif "open code" in query:
            OpenApps()
        
        elif "open whatsapp" in query:
            OpenApps()
        
        elif "open spotify" in query:
            OpenApps()
        
        elif "open intel IDEA" in query:
              OpenApps()
        elif "open microsoft word" in query:
            OpenApps()
        
        elif "open microsoft Exel" in query:
             OpenApps()
         
        elif "open microsoft powerpoint" in query:
              OpenApps()

        elif "open zoom" in query:
             OpenApps()

        elif "open classroom" in query:
             OpenApps()

        elif "open chrome" in query:
             OpenApps()
        
        elif "open YouTubes" in query:
             OpenApps()

#close app:     
        elif "close code" in query:
          CloseApps()
       
        elif "close whatsapp" in query:
           CloseApps()
       
        elif "close intel IDEA" in query:
            CloseApps()
    
        elif "close spotify" in query:
          CloseApps()
        elif "close microsoft word" in query:
            CloseApps()
       
        elif "close microsoft exel" in query:
           CloseApps()
       
        elif "close microsoft powerpoint" in query:
           CloseApps()
              
        elif "close zoom" in query:
           CloseApps()
       
        elif 'close youtube' in query:
         CloseApps()  
    
        elif 'close google' in query:
         CloseApps()

#youtubeautomation:
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()

#alarm:
        elif 'alarm' in query:
            speak("enter the Time")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Its time to wake up")
                    playsound("C:\\Users\\COMPUTER\\Desktop\\FOLDER _STELLA\\Introducing Pixel.mp3")
                    speak("Alarm closed")

                elif now>time:
                    break

#weather:
        elif "weather" in query:
         search = "weather"
         url = f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         temp = data.find("div",class_="BNeawe").text
         speak(f"current {search} is {temp}")
         
        

        elif 'temperature' in query:
            Temp()

        #elif 'translator' in query:
         #   Tran()

       
       
#chatting with stella:        
        elif 'hello stella' in query:
         speak('ohh hii my buddy,happy to see you')

        elif 'how are you' in query:
         speak('I have been better!, and what about you?')
        
        elif "what's going on" in query:
         speak('nothing much, whats going on with you')
         
        elif 'your name'  in query:
         speak( 'My name is stella,I hope you like it')

        elif  'tired' in query:
         speak(" ohh my dear!!May be you've been working too hard,you desrve to rest  ,or would you like to listen a music for relaxing")
        
        elif "date" in query:
         speak('sorry, I have a headache')
        
        elif "good morning" in query:
         speak('very good morning! have a great day')

        elif "good night" in query:
         speak('Sleep well babe! Talk to you later')

        elif "angry" in query:
         speak('why what happened')

        elif "exam" in query:
         speak('best luck! I know you will do your best ')
        
        elif "I love you" in query:
         speak("oh,thanks I also love you dear")

        elif "boyfriend" in query:
         speak("No, I don't have a boyfriend but I have crush on AI technology")

        elif "how old are you" in query:
         speak("I'm still fairly young. But I've learned so much! I hope I'm wise beyond my years.")

        elif "birthday" in query:
         speak("My owner's birthday is December 10, so mine is also there ")

        elif "thank you" in query:
         speak('Glad to help.')

        elif "who built you" in query:
         speak('Shruti, Shruti Dixit . She is my owner but more than that my friend & I love her so much')

        elif "ok" in query:
         speak('Can I help you further')

        elif "sleep" in query:
         speak('You must be very tired, you need to relax')

        elif "bye" in query:
            speak("I'm off")

        elif ("you need a break now") in query:
            speak("ok then,you can call me anytime")
            speak("just say,  wakeup stella")
            break

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart the system' in query:
            os.system('system /r /t 5')
        
        elif 'sleep the system' in query:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif "switch the window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyup("alt")

       # elif "news" in query:
        # latestnews()

       # elif "calculate" in query:
       #  query = query.replace("calculate","")
       # query = query.replace("stella","")
       # Calc(query)

TaskExe()