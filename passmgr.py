from cryptography.fernet import Fernet
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
# import wikipedia as wk



# module that will allow to encrypt the texts.

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("What is the master password? ")
# key = load_key() + master_pwd.encode()
key = load_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''



def view():
    with open('passwords.txt', 'r') as r:
        for line in r.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User: ", user , "| Password: " , fer.decrypt(password.encode()).decode())


    

b'Hello'

def add():
    name = input("Account name: ")
    pwd = input("Password: ")


    with open('passwords.txt', 'a') as r:
        r.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def talk(text):
    engine.say(text)
    engine.runAndWait()




while True:

    mode = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    print('Welcome to the Password Encryption project created by Parul and Aman.')
    engine.runAndWait()
    print('Here you can create account and your password will be stored in the encrypted format')
    engine.runAndWait()


    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = mode.listen(source)
            command = mode.recognize_google(voice)
            command = command.lower()
            text = str(command)
            print(command)

    except:
        pass
    
    # mode = input("Would you like to add a new password or view existing ones?(view, add), press q to quit? ").lower()
    
    
    if 'quit' in text:
        break

    if 'play' in text:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    if 'view' in text:
        view()

    elif 'ad' in text:
        add()

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    else:
        print("Invalid mode")
        continue

