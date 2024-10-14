import speech_recognition as sr
from deep_translator import GoogleTranslator as translator

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
with sr.Microphone() as source:
    print("Listening....")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("What you spoke in English is:",text)
        lang = input("Which language should I translate it to?: ")
        translated = translator(source='auto', target=lang).translate(text)
        print("The content in",lang,"is:",translated)
    except:
        print("Encountered an error!")
