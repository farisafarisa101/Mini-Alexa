import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import flask
import webbrowser
from datetime import date

engine=pyttsx3.init()
engine.setProperty("rate",150)
voice= engine.getProperty("voice")
engine.setProperty('voice',voices [1].id)
recognizer=sr.Recognizer()
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
def run_alexa():

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration)
        print('\n')
        print("Start Speaking")
        engine_talk('listening....')
        recordedaudio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(recordedaudio,language='en-in')
        command=command.lower()
        if 'alexa' in command:
            command=command.replace('alexa','')
            print('You Said :'+command)
        if 'Hello' in command:
            print('Hello ...How can i Help you?????')
            engine_talk('Hello ...How can i Help you?????')
        elif 'Who are you' in command:
            print('I am mini alexa a k a your virtal assistant master. How can I help you')
            engine_talk('I am mini alexa a k a your virtal assistant master. How can I help you')
        elif 'Can you do' in command:
            print('''I can Paly songs on youtube,tell you a joke, search on wikipedia,tell date and time ,find your location,locate area on map,open different websites like instagram ,youtube,gmail,git hub,stack overflow and searches on google.How may I help you???''')
            engine_talk('''I can Paly songs on youtube,tell you a joke, search on wikipedia,tell date and time ,find your location,locate area on map,open different websites like instagram ,youtube,gmail,git hub,stack overflow and searches on google.How may I help you???''')
        elif 'play' in command:
            song.command.replace('Plya','')
            print('Playing ',+song)
            engine_talk('Playing', +song)
            pywhatkit.playonyt(song)
        elif 'Date and Time' in command:
            today=date.today()
            time =datetime.datetime.now().strftime('%I:%M:%H')
            #Textual Month, Day and Year
            d2=today.strftime('%I,%M,%H')
            print("Today's Date is ",d2,'Current time is ',time)
            engine_talk('Current Time is '+time)
            engine_talk('and Today is :'+d2)
        elif 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M:%p')
            print('Current Time is :',+time)
            engine_talk('Current time is')
            engine_talk(time)
        elif 'date' in command:
            today=date.today()
            print("Today's Dtae:",today)
            #textual month ,day and Year
            d2=today.strftime("%B,%d,%Y")
            print("Today's Date is:",d2)
            engine_talk("The Today's Date is")
            engine_talk(d2)
        elif 'Tell Me About' in command:
            name=command.replace('Tell me about ','')
            info=wikipedia.summary(name,1)
            print(info)
            engine_talk(info)
        elif 'Wikipedia' in command:
            name = command.replace('Wikipedia ', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'What is ' in command:
            name = command.replace('What is ', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'Who is ' in command:
             name = command.replace('Who is  ', '')
             info = wikipedia.summary(name, 1)
             print(info)
             engine_talk(info)
        elif 'What is ' in command:
            search='https://www.google.com/search?q='+command
            print('Here is what i Found on Internet.....')
            engine_talk('Searching......Here is What i Found on Internet....')
            webbrowser.open(search)
        elif 'Joke' in command:
            _joke=pyjokes.get._joke()
            print(_joke)
            engine_talk(_joke)
        elif 'Search' in command:
            search='https://www.google.com/search?q='+command
            engine_talk('Searching....')
            webbrowser.open(search)
        elif 'My Locaion' in command:
            url="https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            engine_talk("You must be somewhere near here, as per Google maps")
        elif 'locate' in command:
            engine_talk('Locating.....')
            loc=command.replace('locate','')
            if 'On Map' in loc:
                loc=loc.replace('On Map','')
            url="https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            print('Here is the Location of ',+loc)
            engine_talk('Here is the Location of ',+loc)
        elif 'On Map' in command:
            engine_talk('Locating.....')
            loc=command.split("")
            print(loc)
            url='https://google.nl/maps/place/'+loc[1]+'/&map;'
            webbrowser.get().open(url)
            print('Here is the Location of '+loc[1])
            engine_talk('Here is the Location of '+loc[1])
        elif 'Location of' in command:
            engine_talk('Locating.....')
            loc=command.replace('Find Location of ','')
            url = 'https://google.nl/maps/place/' + loc + '/&map;'
            webbrowser.get().open(url)
            print('Here is the Location of ' + loc)
            engine_talk('Here is the Location of ' + loc)
        elif 'Where is ' in command:
            engine_talk('Locating.....')
            loc = command.replace('Where is  ', '')
            url = 'https://google.nl/maps/place/' + loc + '/&map;'
            webbrowser.get().open(url)
            print('Here is the Location of ' + loc)
            engine_talk('Here is the Location of ' + loc)
        elif 'BootCamps' in commad:
            search='http://tathastu.twowaits.in/index.html#courses'
            engine_talk('opening boot camps')
            webbrowser.open(search)
        elif 'boot camps' in command :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            engine_talk('opening boot camps')
            webbrowser.open(search)
        elif 'python bootcamp' in command :
            search = 'http://tathastu.twowaits.in/kickstart_python.html'
            engine_talk('showing pythonboot camp')
            webbrowser.open(search)
        elif 'data science bootcamp' in command :
            search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
            engine_talk('showing data science and ml bootcamp')
            webbrowser.open(search)
        elif 'Open Google' in command:
            print('Opening Google............')
            engine_talk('Opening Google')
            webbrowser.open_new('https://www.google.co.in/')
        elif 'Open Gmail' in command:
            print('Openning Gmail....')
            engine_talk('Opennig Gmial')
            webbrowser.open_new('https://mail.google.com/')
        elif 'Open Youtube' in Command:
            print("Openning Youtube....")
            engine_talk('Openning Youtube....')
            webbrowser.open_new('https://www.youtube.com/')
        elif 'Open Instagarm' in Command:
            print('Openning Instagram...')
            engine_talk('Openning Instagram......')
            webbrowser.open_new('https://www.instagram.com/')
        elif 'Open Stack Overflow' in command:
            print('Openning Stack Overflow')
            engine_talk('Openning Stack Overflow')
            webbrowser.open_new('https://www.stackoverflow.com/')
        elif 'Open github' in command:
            print('Openning git hub.....')
            engine_talk('Openning git hub.....')
            webbrowser.open_new('https://github.com/')
        elif 'Bye' in command:
            print('Good Bye, Have a nice Day!!!!')
            engine_talk('Good Bye, Have a nice Day!!!')
            sys.exit()
        elif 'Thank You' in command:
            print('Your Welcome')
            engine_talk('Your Welcome')
        elif 'Stop' in command:
            print('Good Bye, Have a nice Day!!!!')
            engine_talk('Good Bye, Have a nice Day!!!')
            sys.exit()
        elif 'Tata' in command:
            print('Good Bye, Have a nice Day!!!!')
            engine_talk('Good Bye, Have a nice Day!!!')
            sys.exit()
        else:
            print('Here is What i Found on Internet....')
            engine_talk('Here is What i Found on Internet.....')
            search='https://www.google.com/search?q='+command
            webbrowser.open(search)
    except Exception as ex:
        print(ex)
print('Clearing Background Noise.....Please Wait')
engine_talk('Clearing Background Noise.....Please Wait')
print('\n')
print('Hello i am Mini Alexa ,How can i help you???')
engine_talk('Hello i am Mini Alexa ,How can i help you???')

while True:
    run_alexa()
