import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from langdetect import detect

# Voice response using gTTS
def speak_response(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Get user voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results.")
        return ""

# Detect the language of input text
def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

# Main chatbot logic (sample flow)
if __name__ == "__main__":
    user_input = get_voice_input()
    lang = detect_language(user_input)

    if "book" in user_input.lower():
        response = "You can search for books by title or author."
    elif "location" in user_input.lower():
        response = "The library is located on the main campus near the ICT Centre."
    elif "hours" in user_input.lower():
        response = "The library is open from 8 AM to 10 PM on weekdays."
    elif user_input.strip() == "":
        response = "I did not catch that. Please try again."
    else:
        response = "I am here to help you with your library needs."

    speak_response(response, lang)