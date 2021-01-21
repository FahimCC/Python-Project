import smtplib  # simple mail transfer protocol library
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()   # transport layer security
    server.login('ffsmile143@gmail.com', '***********')   # **** = password
    email = EmailMessage()
    email['From'] = 'ffsmile143@gmail.com'
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
    # server.sendmail('ffsmile143@gmail.com', 'ffnasif@gmail.com', 'Assalamu Alaikum. I am Nuren. I wanted to marriage you very quickly. In Sha Allah.')


def get_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            print('Voice catch')
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        print('no voice')
        pass


email_list = {
    'Fahim': 'ffnasif@gmail.com',
    'Nuren': 'nurenabha@gmail.com'
}


def get_email_info():
    talk("To whom you want to sent email")
    name = get_command()
    receiver = email_list[name]
    print(receiver)

    talk("What is the subject of your email?")
    subject = get_command()

    talk("Tell me the text in your email")
    message = get_command()

    send_email(receiver, subject, message)
    talk('Hei, lazy dude. Your mail is sent.')
    talk('Do you want to sent more email?')
    if 'yes' in get_command():
        get_email_info()


get_email_info()
print('Thank you')