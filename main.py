import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import requests, json , sys

listener = sr.Recognizer() #Speech Recognition Constant
alexa = pyttsx3.init() #covert text to speach
voices = alexa.getProperty('voices') #added default voices
alexa.setProperty('voice', voices[1].id) #set as a female voice

def talk(text): #take text as a perameter then speak the text & wait
    alexa.say(text)
    alexa.runAndWait()


def weather(city): #weather used openweathermap api take city name as input
    # API key
    api_key = "e109b74f2efd786c4194d0efb32c9211"
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # city name
    city_name = city

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        return str(current_temperature)

def take_command(): #take command from user
    try:
        with sr.Microphone() as source: #add  microphone as listener
            print('Listening...')
            voice = listener.listen(source) #listen from Microphone
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command: #run only whene someone use alexa word
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa(): #execute take_command function through various condition
    command = take_command()
    if 'time' in command: #speck date & time
        time  = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command: #play youtube video used pywhatkit library
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command: #read from wikipedia used wikipedia library
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)

    elif 'joke' in command: #tell jokes used pyjokes library
        talk(pyjokes.get_joke())

    elif 'message' in command: #message in whatsapp used pywhatkit library
        pywhatkit.sendwhatmsg("+8801757110249","This is a message",15,00)

    elif 'weather' in command: #weather In location
        weather_api = weather('Sylhet') #pass city name in weather api function
        talk(weather_api + 'degree fahreneit')

    else:
        talk('I did not get it but I am going to search it for you') #search at google used pywhatkit library
        pywhatkit.search(command)

while True: #run alexa continuously -> take command from user one after another
    run_alexa()