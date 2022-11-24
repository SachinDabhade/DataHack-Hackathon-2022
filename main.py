import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr

"""The main speaking engine is here"""
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 30)

def Take_Command(name) -> str:
    """It simply take command from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 2
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"{name} said: {query}\n")
    except Exception as error:
        print("Please speak clearly...")
        speak("Please speak clearly...")
        return "None"
    return query


def wiki(query) -> str:
    print('\n********** Searching Publically Available Information...! **********\n')
    query = query.strip().split(' ')
    query = " ".join(query[0:])
    if query == 'None':
        return None
    record_query(query)
    if 'wikipedia' in query:
        query = query.replace("wikipedia", "")
    query = wikipedia.search(query)
    if query:
        print('----- OPTIONS -----')
        loop(query)
        print('----- OPTIONS -----')
        speak('Choose from the above options')
        option = int(input('\nChoose from the above options (Only numerical value): '))
        print("\nSearching about "+query[option-1], end='\n')
    results = wikipedia.summary(query[option-1], sentences=3)
    record_result(results)
    speak("Alright, According to my knowledge")
    print(results)
    speak(results)
    speak('That\'s it')

def speak(audio):
    """It is used to speak the audio output"""
    engine.say(audio)
    engine.runAndWait()

def loop(data) -> None:
    for i, d in enumerate(data):
        print(i+1, d)

def login() -> None:
    """General Login of the user"""
    with open("record.txt", "a") as f:
        f.write(f"Automated Identity Search Tool is started on {datetime.datetime.now()}\n")

def record_query(query) -> None:
    """Get the data for data analysis which is collected by this function"""
    with open("queries.txt", "a") as f:
        f.write(f"{query} : command on {datetime.datetime.now()}\n")

def record_result(result):
    """Get the data for data analysis which is collected by this function"""
    with open("results.txt", "a") as f:
        f.write(f"{result}\n")

if __name__ == '__main__':
    try:
        login()
        print('\n******************* WELCOME TO AUTOMATED IDENTITY SEARCH TOOL *******************')
        while True:
            print('\nSearch any \'person\' or \'organization\': ')
            speak('Search any person or organization ')
            # cmd = Take_Command("User").capitalize()
            cmd = input('\nSearch any person or organization: ')
            wiki(cmd) 
    except Exception as E:
        speak('record did not found, please try again with different name')
        print('\n************************************ THANK YOU *************************************\n')