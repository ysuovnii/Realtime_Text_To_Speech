import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

print("Path of the file: ")
file_path = input() 

try:
    with open(file_path, "r") as r:
        content = r.read()
        print(content)
        engine.say(content)
        engine.runAndWait()
except FileNotFoundError:
    print("Error: File Not Found!")
