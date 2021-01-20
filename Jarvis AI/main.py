import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


listener = sr.Recognizer()
jarvis = pyttsx3.init()
voices = jarvis.getProperty("voices")
jarvis.setProperty("voice", voices[0].id)


def talk(text):
    print(text)
    jarvis.say(text)
    jarvis.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("Please say somthing, i am listening...")
            # print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print("voice catch")
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace("jarvis", "")
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if "assalamu alaikum" in command:
        talk("waalaikum assalam")
    elif "hi" in command:
        talk("hello")
    elif "hello" in command:
        talk("hi")
    elif 'tell me about you' in command:
        talk("I am Jarvis. Created by Fahim Faysal with the help of Allah")
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I %M %p")
        talk("Current time is" + time)
    elif 'play' in command:
        song = command.replace("play", "")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace("tell me about", "")
        info = wikipedia.summary(look_for, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("I did not get it. But I am going to search it for you")
        pywhatkit.search(command)


talk("Assalamu alaikum")
while True:
    run_jarvis()