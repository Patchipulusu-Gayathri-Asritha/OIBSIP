# VOICE ASSISTANT

from requests import get
from translate import Translator
import datetime
import pyaudio
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import time
import webbrowser
import wikipedia

master="Madam"
print("Preparing SHAAN ....\n")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if (hour>0 and hour<6) or (hour>=23):
        print("Hey Owl")
        speak("Hey Owl")
    elif hour>=6 and hour<12:
        print("Good Morning "+master)
        speak("Good Morning "+master)
    elif hour>=12 and hour<18:
        print("Good Afternoon "+master)
        speak("Good Afternoon "+master)
    else:
        print("Good Evening "+master)
        speak("Good Evening "+master)

    print("\nI am SHAAN, A Voice Assisstant")
    print("Please tell me, How may I help you?")
    
    speak("I am SHAAN, A Voice Assisstant")
    speak("Please tell me, How may I help you?")

def takeCommand():
    print("\n..............................................................................................................................................................................\n")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('\nListening the Request...')
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print('\nRecognising the Request..')
        query=r.recognize_google(audio,language='en-in')
        print(f"Your Message is : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again Please ...")
        speak('Please Say that again')
        query="None"
    return query

def screenshot():
    pic=pyautogui.screenshot()
    file_name=datetime.datetime.now().strftime("%H-%M")+" .png"
    pic.save(file_name)
    print("Screenshot Saved as "+file_name)
    speak("Screenshot Saved as "+file_name)
             
def sayJoke():
    joke=pyjokes.get_joke(language='en',category='all')
    print('\nThe Joke is : ')
    print(joke)
    speak(joke)

        

if __name__=="__main__":
    wishMe()
    con=1
    while con!=2:
        query=takeCommand().lower()

        if 'hello' in query:
            print('Hi '+master)
            speak('Hi '+master)

        elif 'how are you' in query:
            speak('I am Good. Thanks for asking')
            speak('How can I help you ?')

        elif 'your name' in query:
            speak('I am SHAAN, your Voice Assisstant')
            speak('Your Good Name Please')
            print('I am SHAAN, your Voice Assisstant')
            print('Your Good Name Please !')

        elif 'my name' in query:
            query=query.replace('my name is ','')
            speak('Good to see you '+query+' !')

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H: %M: %S")
            print("\nThe Time is : ",strTime)
            speak(f"{master}, The Time is : {strTime}")

        elif 'screenshot' in query:
            screenshot()

        elif 'joke' in query:
            sayJoke()

        elif 'translate' in query:
            speak('What do you like to translate?')
            text=takeCommand().lower()
            translator=Translator(from_lang="en",to_lang="it")
            translation=translator.translate(text)
            speak('Translated Text is : ')
            speak(translation)
            print('Italian Translation is :\n')
            print(translation)

        elif 'search wikipedia' in query:
            try:
                speak('What do you want to Search?')
                search=takeCommand().lower()
                speak('Searching Wikipedia ...')
                results=wikipedia.summary(search,sentences=2)
                speak('According to Wikipedia')
                print("\nResults for your Search are : ")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                print('Sorry ! I did not find the result')
                speak('Sorry ! I did not find the result')

        elif 'open whatsapp' in query:
            speak('Opening Whatsapp')
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            speak('Starting YouTube')
            webbrowser.open("youtube.com")

        elif "open linkedin" in query:
            speak('Opening Linkedin')
            webbrowser.open("Linkedin.com")

        elif "open stack overflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")

        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")

        elif 'play youtube' in query:
            speak('What do you like to Watch?')
            search=takeCommand().lower()
            speak('I have got these videos')
            pywhatkit.playonyt(search)

        elif 'search google' in query:
            speak('What do you want to Google?')
            search=takeCommand().lower()
            speak('I got these results')
            pywhatkit.search(search)

        elif 'thank you' in query:
            speak('You are Welcome'+master)
            speak('If you need any assistance, Please ask me')

        elif ('quit' in query) or ('shutdown' in query) or ("exit" in query):
            speak('Good Bye!')
            speak('See you '+master)
            print('Quitting ....')
            quit()

        
            
            

        
        












        
