import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import datetime as dt
import webbrowser

voice_value=0
speech_rate = 180
name = 'Priyanka'

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('rate',speech_rate)
#print(voice)
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 00 and hour < 12:
        speak('Good Morning Sir!,')
    elif hour >=12 and hour < 16:
        speak('Good after noon sir!,')
    elif hour >= 16 and hour < 20:
        speak('Good evening sir!,')
    elif hour >= 20 and hour < 23:
        speak('Good night sir!,')

"""def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said : {query}\n')
    except Exception as a:
        #print(a)

        print('say that again please...')
        return none
    return query"""

def GiveCommand():
    r = input('Listening...')
    #speak(r)
    return r

if __name__ == "__main__":
    wishMe()
    while True:
        query = GiveCommand().lower()
        #print(query)

        if 'search for' in query:
            query = query.replace('search for','')
            speak('Searching on Wikipedia...')
            
            try:
                results = wikipedia.summary(query, sentences=1)
                print(results)
                speak('According to wikipedia...')
                speak(results)
            except:
                speak('There is an error we cant find the link for '+query)
            
        
        elif 'search on' in query:
            if 'google' in query:
                new = 2
                taburl = 'http://google.com/search?q='
                query = GiveCommand().lower()

                data = query.split()
                text1 = []
                text1.append(data[0])
                for i in range(0,len(data)):
                    if data[i] != 'google':
                        text1.append(data[i+1])
                    else:
                        break

                for i in range(0,len(text1)):
                    data[i] = '!'
                for i in range(0, data.count('!')):
                    data.remove('!')

                query = ' '.join(data)
                speak('Searching on google about '+query)
                webbrowser.open(taburl+query, new=new)

            elif 'youtube' in query:

                new = 2
                taburl = 'https://www.youtube.com/results?search_query='
                query = GiveCommand().lower()

                data = query.split()
                text1 = []
                text1.append(data[0])
                for i in range(0,len(data)):
                    if data[i] != 'youtube':
                        text1.append(data[i+1])
                    else:
                        break

                for i in range(0,len(text1)):
                    data[i] = '!'
                for i in range(0, data.count('!')):
                    data.remove('!')

                query = ' '.join(data)
                speak('Searching on youtube about '+query)
                webbrowser.open(taburl+query, new=new)

        elif 'speech rate' in query:
            if 'increase' in query:
                speak('Okay sir! How much you want to keep my speech rate')
                query = GiveCommand().lower()
                res = [int(i) for i in query.split() if i.isdigit()]
                j = int(res[0])
                speech_rate = j
                engine.setProperty('rate',speech_rate)
                speak('Hello Sir I ahve increased my speech rate.')
            elif 'decrease' in query:
                speak('Okay sir! How much you want to keep my speech rate')
                query = GiveCommand().lower()
                res = [int(i) for i in query.split() if i.isdigit()]
                j = int(res[0])
                speech_rate = j
                engine.setProperty('rate',speech_rate)
                speak('Hello Sir I ahve decreased my speech rate.')
        elif 'voice' in query:
            speak('okay Sir! as you want to.')
            engine.setProperty('voice',voice[voice_value].id)
            speak('Do you like this sir?')
            data = 'true'
            while('true'==data):
                query = GiveCommand().lower()
                if 'yes' in query:
                    if voice_value == 0:
                        name = 'Vivek'
                        voice_value=1
                    elif voice_value == 1:
                        voice_value=0
                        name = 'Priyanka'
                    speak('Thank you sir! I am Happy that you like me in this way. Hello Sir I am '+name+'.')
                    data = ''
                elif 'no' in query:
                    if voice_value == 0:
                        voice_value=1
                        name = 'Priyanka'
                    elif voice_value == 1:
                        voice_value=0
                        name = 'Vivek'
                    engine.setProperty('voice',voice[voice_value].id)
                    speak('I have only two versions sir. I am sorry that you did not like my second version.')
                    speak('Hello Sir I am '+name+'.')
                    data = ''
                    if voice_value==0:
                        voice_value=1
                    elif voice_value==1:
                        voice_value=0
                    
        elif 'rest' in query or 'sleep' in query:
            speak('are you sure sir?')
            data='true'
            while(data == 'true'):
                query = GiveCommand().lower()
                if 'yes' in query or 'yup' in query or 'yeah' in query:
                    change = 'yes'
                    speak('Okay sir! when ever you need me I will be here to help you.')
                    while change == 'yes':
                        query = GiveCommand().lower()
                        if 'wake up' in query:
                            speak('I am ready for you sir welcome!')
                            change = 'no'
                            data = ''
                elif 'no' in query:
                    speak('Great sir! say what i have to do?')
                    data = ''
                else:
                    speak('.Can you please repeat that sir?')
        elif 'exit' in query and 'permanently' in query:
            speak('You really sure sir!')
            query = GiveCommand().lower()
            if 'yes' in query:
                speak('okay sir! I am shutting down myself. Have a great day sir!')
                exit()

        elif 'volume' in query:
            if 'decrease' in query:
                res = [int(i) for i in query.split() if i.isdigit()]
                j = int(res[0])
                speak('Okay Sir!,I am decreasing volume by '+str(j)+'%')
                volume = engine.getProperty('volume')
                v = volume-volume*(j/100)
                engine.setProperty('volume',v)
                speak('volume is decreased by '+str(j)+'% sir!')
                      
            elif 'increase' in query:
                res = [int(i) for i in query.split() if i.isdigit()]
                j = int(res[0])
                speak('Okay Sir!,I am increasing volume by '+str(j)+'%')
                volume = engine.getProperty('volume')
                v = volume+volume*(j/100)
                engine.setProperty('volume',v)
                speak('volume is increased by '+str(j)+'% sir!')
        elif 'your name' in query:
            speak('Sir My name is '+name)
        elif 'time' in query:
            
            hh = dt.datetime.now().hour
            mm = dt.datetime.now().minute
            d = dt.datetime.strptime(str(hh)+':'+str(mm), '%H:%M')
            da = d.strftime('%I:%M %p')
            speak('Now time is '+da)
            
        elif 'wake up' in query:
            speak('I am sir! Say, how can i help you?')
        elif 'okay' in query or 'good' in query:
            speak('yes sir')
        elif 'great' in query or 'wow' in query:
            speak('thank you sir!')
        elif 'thank you' in query:
            speak('Your always welcome sir!')
        else:
            speak('Sorry Sir i did not get you please repeat it.')
            
            
            



















