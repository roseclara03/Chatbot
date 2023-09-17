import random
from googletrans import Translator
import pygame
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Dictionary of Onam-related information
onam_knowledge_base = {
    "what is onam": "Onam is a harvest festival celebrated in Kerala, India.",
    "onam songs": "There are many beautiful Onam songs that celebrate the festival.",
    # Add more Onam-related information here
}

# Function to get a random greeting response
def get_greeting():
    greetings = [
        "Hello there, dear friend!",
        "Hiya! What's cookin'?",
        "Greetings, my friend! How's the day treating you?",
        "Hey you! What brings you here today?",
    ]
    return random.choice(greetings)

# Function to ask for the user's name in a funny way
def ask_for_name():
    funny_questions = [
        "Well, hello there! What's your name, superstar?",
        "Hey, do me a favor, will you? Tell me your name and make it sound as awesome as possible!",
        "Greetings, mysterious traveler! Mind sharing your name, or should I call you 'The Enigma'?",
    ]
    return random.choice(funny_questions)

# Function to ask for the user's preferred language
def ask_language_preference():
    print("Maveli: " + get_greeting())
    print("Maveli: " + ask_for_name())
    user_name = input("You: ")
    print(f"Maveli: {user_name}! What language would you like to use for our chat? (Malayalam, English)")
    user_language = input("You: ").lower()
    return user_language

# Function to make Maveli speak the response
def speak_response(response, language_preference):
    if language_preference == "malayalam":
        translator = Translator()
        response = translator.translate(response, src='en', dest='ml').text
        engine.setProperty('voice', 'ml')
    else:
        engine.setProperty('voice', 'en')

    engine.say(response)
    engine.runAndWait()

# Function to handle user queries
def handle_user_query(query, language_preference):
    query = query.lower()
    if query in onam_knowledge_base:
        response = onam_knowledge_base[query]
    elif "history" in query:
        response = "I don't have that information right now, but I can tell you about Onam or share a joke!"
    elif any(greeting in query for greeting in ["hello", "hi", "hey", "hola"]):
        response = get_greeting()
    else:
        response = "I'm not sure how to respond to that."

    if language_preference == "malayalam":
        # Translate the response to Malayalam
        translator = Translator()
        response = translator.translate(response, src='en', dest='ml').text

    return response

# Main loop for Maveli
def main():
    user_language = ask_language_preference()
    print(f"Maveli: You selected {user_language} as your preferred language.")
    print(f"Maveli: {get_greeting()} How can I assist you today?")

    while True:
        user_input = input(f"You: ")
        response = handle_user_query(user_input, user_language)
        print(f"Maveli: {response}")

        # Make Maveli speak the response
        speak_response(response, user_language)

        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main()
