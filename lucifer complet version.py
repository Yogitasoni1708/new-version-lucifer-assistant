import datetime
import webbrowser
from winreg import QueryInfoKey, QueryReflectionKey, QueryValue
import pyttsx3
import pywhatkit
import speech_recognition
import wikipedia
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices)
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 130)


def speak(audio):
                engine.say(audio)
                engine.runAndWait()


def takeCommand():
                r = speech_recognition.Recognizer()
                with speech_recognition.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 4
                    r.energy_threshold = 300
                    audio = r.listen(source, 0, 4)

                try:
                    print("Understanding...")
                    query = r.recognize_google(audio, language='en-us')
                    print(f"You said: {query}\n")
                except Exception as e:
                    print("say it again") 
                    speak("say it again")
                    return "None"     
                return query

if __name__ == "__main__":
                while True:
                    query = takeCommand().lower()
                    if "wake up lucifer" in query:
                        hour = int(datetime.datetime.now().hour)

                        if 0 <= hour <= 12:
                            speak("Good Morning sir, how are you?")
                        elif 0 <= hour <= 12: 
                            speak("Good Afternoon sir, how are you?")

                        else:
                            speak("Good Evening sir, how are you?")

                    while True:
                        query = takeCommand().lower()
                        if "go to sleep lucifer" in query:
                           print("Ok, See you, Remember if you need anything just say, wake up lucifer") 
                           speak("Ok, See you, Remember if you need anything just say, wake up lucifer")

                        elif "I'm good how are you"in query: 
                            speak("I am also good, how may I help you today?")
                        elif "thank you"in query:
                            print("you are welcome dude")
                            speak("You are welcome dude") 
                        elif 'search' in query and 'youtube' in query:
                            speak("this is what i found for you sir")
                            query = query.replace("search","")

                            query = query.replace("on youtube","")
                            query = query.replace("youtube","")
                        
                            web = "https://www.youtube.com/results?search_query="+ query
                            webbrowser.open(web)
                            pywhatkit.playonyt(query)
                            speak("here you go ,sir")

                        elif "google" in query:
                                import wikipedia as googleScrap
                                query = query.replace("lucifer", "")
                                query = query.replace("google search", "")
                                query = query.replace("google", "")
                                speak("This is what I found")
                                try:
                                    pywhatkit.search(query)
                                    result = googleScrap.summary(query, 1)
                                    speak(result)

                                except:
                                    speak("Did not find anything about that, sorry")
                                query = query.replace("youtube", "")
                                query = query.replace("google search", "")
                                query = query.replace("google", "")
                                speak("This is what I found on google")

                        elif "wikipedia" in query:
                                speak("Searching from wikipedia....")
                                query = query.replace("wikipedia", "")
                                query = query.replace("search wikipedia", "")
                                query = query.replace("lucifer", "")
                                results = wikipedia.summary(query,sentences=2)
                                speak("According to wikipedia..")
                                print(results)
                                speak(results)
