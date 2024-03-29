from dis import Instruction
from multiprocessing.connection import Listener
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia


Listener = sr.Recognizer()

machine = pyttsx3.init()


machine.setProperty('rate', 120)
# voices = machine.getProperty('voices')

# for voice in voices:
#     print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

# # Setting the voice
# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# machine.setProperty('voice', voice_id)

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global Instruction
    try:
        with sr.Microphone() as origin:
            print("listening...")
            speech = Listener.listen(origin)
            Instruction = Listener.recognize_google(speech)
            Instruction = Instruction.lower()
            if "charlie" in Instruction:
                Instruction = Instruction.replace('charlie', '')
                print(Instruction) 
            print(Instruction)


    except:
        pass
    return Instruction


def play_charlie():
    Instruction = input_instruction()
    print(Instruction)
    if "play" in Instruction:
        song = Instruction.replace('play', "") 
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in Instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time is' + time)

    elif 'date' in Instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date is" + date)

    elif 'how are you' in Instruction:
        talk('I am Fine, What about you?')

    elif 'What is your name' in Instruction:
        talk('Hi! I am charlie, How can I help you?')
    
    elif 'Who is' in Instruction:
        human = Instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk('Please repeat')
    
    
play_charlie()
