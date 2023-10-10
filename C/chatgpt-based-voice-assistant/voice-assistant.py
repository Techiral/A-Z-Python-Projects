import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def speak_text(text):
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

intro_message = "Hello, I am your voice assistant. How can I assist you today?"
speak_text(intro_message)

recognizer = sr.Recognizer()

def record_and_transcribe():
    while True:
        try:
            
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = recognizer.listen(source)
                
                
                user_input = recognizer.recognize_google(audio)
                return user_input
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")

def get_response(user_input, chat_history):
    
    chat_history.append({"role": "user", "content": user_input})

    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    
    assistant_response = response.choices[0].message.content
    return assistant_response


chat_history = [{"role": "system", "content": "You are now chatting with a voice assistant."}]

while True:
    
    user_input = record_and_transcribe()
    print(f"User: {user_input}")
    input_length = len(user_input)
    assistant_response = get_response(user_input, chat_history)
    final_response = f"Your input was {input_length} characters long. Assistant: {assistant_response}"
    print(f"Assistant: {final_response}")
    speak_text(final_response)
