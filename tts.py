import speech_recognition as sr 

rec = sr.Recognizer()
mic = sr.Microphone()

run = True
while run: 
    with mic as source: 
        print("Listening...")
        rec.adjust_for_ambient_noise(source, duration=0.5)
        audio = rec.listen(source)
    try: 
        text = rec.recognize_google(audio)
        print("You said: ", text)
        
        with open("audio.txt", "a") as f: 
            f.write(text + "\n")

        if text.strip().lower() == "stop": 
            print("---Stopped Listening---")
            run = False

    except sr.UnknownValueError: 
        print("Error: Could not understand")

