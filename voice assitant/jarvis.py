import speech_recognition as aa     # pip install SpeechRecognition
import pyttsx3                      # pip install pyttsx3
import pywhatkit                    # pip install pywhatkit
import datetime                     # pip install datetime
import wikipedia                    # pip install wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()
 

def input_instruction(): 
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech, language="id-ID")
            instruction = instruction.lower()
            if "Jarvis" in instruction:
                instruction = instruction.replace('jarvis', " ")
                print(instruction)

    except:
        pass
    return instruction

def play_Jarvis():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', " ")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time' + time)
        print('Time: ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date" + date)
        print("Today's date " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
        print('I am fine, how about you?')
    
    elif 'what is your name' in instruction:
        talk("I am Jarvis, what can i do for you?")
        print ('I am Jarvis, what can i do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        talk(info)
        print(info)

    else:
        talk("Please repeat")
        print("Please repeat")

play_Jarvis()