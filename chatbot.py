import random
import re
import tempfile
import os
import pygame
import pyttsx3


engine = pyttsx3.init()


pygame.mixer.init()


def greet_user():
    engine.say("Namaskaram! I am Mahabali,What is your name my dear? ")
    engine.runAndWait()

    print("Maveli:Namaskaram! I am Mahabali,What is your name my dear? ")  
    user_name = input("You: ")  
    print(f"Namaskaram, {user_name}! How can I help you? If you have any questions for me, type 'questions'. If you need to change the language, type 'language'. If you want to exit, type 'bye'.")
    engine.runAndWait()
    engine.say(f"Namaskaram, {user_name}! How can I help you? If you have any questions for me, type 'questions'. If you need to change the language, type 'language'. If you want to exit, type 'bye'.")
    engine.runAndWait()

    return user_name


knowledge_base = {
    "what is onam": {
        "responses": {
            "english": "Onam is an annual Indian harvest and cultural festival related to Hinduism ,celebrated mostly by the people of Kerala but now ireespective of caste ,creed and religion ever people n kerala celebrate onam. A major annual event for Keralites, it is the official festival of the state and includes a spectrum of cultural events. Onam commemorates King Mahabali and Vamana.",
            "malayalam": "Onam malayalikalude hindhava mathavumay bandhapetta parambaragathamaya oru vilavidup agoshaman enkolum jaathi matha bedha manye keralathile ellarum onam agoshikunu. Keralathinte etavum pradhanyamulla agosham an onam athil koreye achara anushtanangal ulpedunnu. Onam mahabaliyude vamanantem varavine soochipikunu",
        },
        "questions": [
            "tell me about onam",
            "nthan onam",
            "aran kooduthalum onam agoshikkunath",
            "onam",
            "significance of onam"
        ],
    },
    "onam sadhya": {
        "responses": {
            "english": "Onam Sadhya is the grand feast served during the Onam festival. It consists of a variety of traditional vegetarian dishes, including rice, sambar, avial, and more. The feast is served on a banana leaf and is an essential part of Onam celebrations.",
            "malayalam": "Onam sadhya onathinod anubandhich vilambuna oru gambeera virunn an. Athil sambar, aviyal, poleyulla palavdiha vibhvangalum ond. Onam Sadya vilumbannath vazhayililan ath virunninte etom pradhanamaya gadakam an",
        },
        "questions": [
            "What is Onam Sadhya, and why is it significant?",
            "what is onam sadhya",
            "Can you name some dishes served in Onam Sadhya?",
            "How is Onam Sadhya traditionally served?",
            "nthan onam sadhya",
            "nthoke vibhavngal an onam sadhya il ullath",
            "onam sadhya",
        ],
    },
    "onam pookalam": {
        "responses": {
            "english": "Pookalam is an intricate and colourful arrangement of flowers laid on the floor. Tradition of decorating Pookalam is extremely popular in Kerala and is followed as a ritual in every household during ten-day-long Onam celebrations from the day of atham.",
            "malayalam": "Onam Pookalam pookalude bangiyil nilath orukki veed alankarikunna oru achararaman. Ee acharam keralathile mikka veedukalilum thudarnu varunnond.Atham muthal path divsthek onam pookal idum",
        },
        "questions": [
            "What is Onam Pookalam, and why is it made?",
            "what is onam pookalam",
            "How are Pookalams created?",
            "what is onam?",
            "what is flower carpet?",
            "flower carpet",
            "onam pookalam",
            "nthan pookalam",
            "nthan onam pookalam",
        ],
    },
    "onam games": {
        "responses": {
            "english": "Onam Games, known as 'Onakalikal' in Malayalam, are traditional sports and games played during Onam. These include boat races, tug-of-war, archery, and various cultural competitions. Onakalikal add excitement to the festival.",
            "malayalam": "Onathile kalikale'Onakalikal' enna parayunnath.Pandmuthalke onathin kalich verunn kalikal an iva. Ithil vallam kali,vadamvali uri adi ennivayan pradhanamya kalikal. Ith Onathinte aaravam erattiyakum.",
        },
        "questions": [
            "What are Onakalikal, and how are they celebrated?",
            "what are onam kalikal",
            "nthan onam kalikal",
            "Can you name some traditional Onam games?",
            "onam kalikal",
            "onam games",
            "onam sports",
            "kalikal"
            ,
        ],
    },
    "onam legends": {
        "responses": {
            "english": "Myself maveli or mahabalii is a beloved mythical king  born in Kerala.  I was known for my righteousness and equality, bringing prosperity and happiness to his kingdom. Lord Vishnu incarnated as a Brahmin boy named Vamana and asked for land that he could cover in three steps. I agreed but was amazed when Vamana grew to encompass the universe in two steps. Realizing Vamana's divinity, I offered my head for the third step, which sent me to the netherworld with the promise of an annual visit.",
            "malayalam": "Mahabali adhava maveli enna njan oru sankalipika rajav an.Njan barichirunna sthalath manushyathavum sambal samridhiyum kond varan njan ennum shredhirunnu. Vishnu Devan oru Brahmina kuttiyude veshathil avatharam edthu vannit oru moon adi mann chodhichu.Njan sammadhichu pakshe vamanan rand adi vechapozhekm prapancham muzhuvan adiyilayi.Ith kand njan moonamthe adi ente shirasil vechukollan parnju angne njan pathalathilek poi.Ithin anusruhtmayitan ella varshavam njan ente prajakale kanan varunnath.",
        },
        "questions": [
            "What are the prominent legends associated with Onam?",
            "Onam legend",
            "Onam charithram",
            "charithram",
            "legend of onam",
            "history of onam",
            "nthan onathinte charithram",
            "Onam nthine soochipikkunu",
            "aaran mahabali",
            "mahabali",
            "Maveli",
            "vamanan",
            "who is mahabali",
            "who is maveli",
            "who is vamanan",
            "vishnu",
            "lord visnu",
            "Tell me the story of King Mahabali and his connection to Onam.",
            "Are there any other mythological stories related to Onam?",
        ],
    },
    "onam attire": {
        "responses": {
            "english": "Onam attire, known as 'Onakodi,' is traditional clothing worn during the festival. Men wear 'Mundu' and 'Shirt' or 'Veshti,' while women adorn themselves in beautiful sarees. The attire reflects Kerala's rich cultural heritage.",
            "malayalam": "Onathile vasthram, 'Onakodi' enna peru aanu. Purushanmar 'Mundu'  athava 'Veshti' kondu. Sthreekal 'kerala saree' udukunu. Penkuttikal pattu pavada allenkil half saree an udukarullath.",
        },
        "questions": [
            "What is Onakodi, and why is it significant during Onam?",
            "onam attire,",
            "onam kodi",
            "onam dress",
            "kodi",
            "How do men and women traditionally dress for Onam?",
            "nthan onathinte vasthram",
            "nthan onathin ellarm dharikar ullath",
        ],
    },
    "onam duration": {
        "responses": {
            "english": "Onam is typically celebrated for 10 days, but the grand festivities usually span over four days. The main day of Onam, known as 'Thiru Onam,' falls on the second day of the festival. It occurs during the Malayalam month Chingam.",
            "malayalam": "Onam sadharanathil 10 dinaangal olla uthsavamaanu, avasanathe nalu divsam an etom agoshakramay acharikkunath. Onathile mukhya dinam thiru onam an. Chinga masathilan onam nadakrullath",
        },
        "questions": [
            "How many days is Onam usually celebrated?",
            "Which is the main day of Onam?",
            "duration",
            "kalavadhi",
            "divsangal",
            "thiruvonam",
            "ethra divsm an onam",
            "when does onam fall",
            "epozhan onam",
        ],
    },
    "onam songs list": {
        "responses": {
            "english": "Some popular Onam songs include 'Thiruvona Kaineettam,' 'Ponnona Tharangini,' 'Onapattin Thalam Thullum,' and 'Maveli Nadu Vaneedum Kalam.' These songs capture the essence of Onam and are sung with great enthusiasm during the festival.",
            "malayalam": "Onathinte prasiddha paattukalil 'Thiruvona Kaineettam,' 'Ponnona Tharangini,' 'Onapattin Thalam Thullum,' ullkkoru sthanam undu. Ithu Onathinte thanath bhavam prakadpikunund. Ellavrm ulsahathode padunna pat an onam pat.",
        },
        "questions": [
            "Can you list some popular Onam songs?",
            "Onam paat",
            "paat",
            "songs",
            "Onam songs",
            "chila onam paatu ethellam",
            "onam paat nthan",
            "nthan onam paat",
            "Tell me the names of famous Onam songs.",
            "Which songs are commonly sung during Onam?",
        ],
    },
    
}

def preprocess_query(query):
    return re.sub(r'\s+', '', query.lower())



def speak_in_english(text):
    engine.say(text)
    engine.runAndWait()

def speak_in_malayalam(text):
    engine.setProperty('rate', 110)
    engine.say(text)
    engine.runAndWait()


def speak_response(response, language_preference):
    
    print(response)
    
    
    response_without_prefix = response.replace("Maveli:", "").strip()

    if language_preference == "malayalam":
        speak_in_malayalam(response_without_prefix)
    else:
        speak_in_english(response_without_prefix)



def handle_user_query(query, language_preference):
    response = ""

    if query.lower() == "language":
        response = "Maveli: You can change the language preference to 'English' or 'Malayalam' by typing 'English' or 'Malayalam'."
    elif query.lower() == "english":
        language_preference = "english"
        response = "Maveli: Language preference set to English."
    elif query.lower() == "malayalam":
        language_preference = "malayalam"
        response = "Maveli: basha malayalathilek aki,ningak ini nerit chodyam choykavunnathan"
    elif query.lower() == "questions":
        response = "Maveli: You can ask me questions about Onam."
    elif query == "bye":
        response = "Maveli: Goodbye! Have a great day!"
        speak_response(response, language_preference)
        exit() 
    else:

        onam_attire_phrases = [
            "attire", "vesham", "dress", "vasthram", "onakodi", "kodi",
            "onam kodi", "vasthrangal", "veshangal", "atires", "dresses",
            "onakodikal", "saree"
        ]
        if any(keyword in preprocess_query(query) for keyword in onam_attire_phrases):
            response = knowledge_base["onam attire"]["responses"][language_preference]
            
        else:
            
            onam_songs_phrases = [
                "paat", "pat", "onapat", "song", "songs", "list songs", "onappat", "onam paat", "onam pat"
            ]
            if any(keyword in preprocess_query(query) for keyword in onam_songs_phrases):
                response = knowledge_base["onam songs list"]["responses"][language_preference]
            else:
                
                onam_pookalam_phrases = [
                    "pookalam", "poo", "flower", "flowers", "flowercarpet",
                    "onapookalam", "flower carpet", "pookalams"
                ]
                if any(keyword in preprocess_query(query) for keyword in onam_pookalam_phrases):
                    response = knowledge_base["onam pookalam"]["responses"][language_preference]
                else:
                    
                    onam_legend_phrases = [
                        "legend", "legends", "myth", "mythology", "history", "charithram",
                        "onacharithram", "maveli", "mahabali", "vamanan", "vishnu",
                        "vishnu devan", "devan", "king", "rajav", "praja", "evil",
                        "evilking", "significance of onam"
                    ]
                    if any(keyword in preprocess_query(query) for keyword in onam_legend_phrases):
                        response = knowledge_base["onam legends"]["responses"][language_preference]
                    else:
                        
                        onam_game_phrases = [
                            "games", "sports", "game", "kali", "onakali", "onam kali",
                            "kalikal", "onakalikal", "vadamvali", "tug of war",
                            "uri adi", "uriadi", "vallamkali", "boatrace"
                        ]
                        if any(keyword in preprocess_query(query) for keyword in onam_game_phrases):
                            response = knowledge_base["onam games"]["responses"][language_preference]
                        else:
                            onam_sadhya_phrases = [
                                "sadhya", "sadya", "feast", "virunn", "vibhavangal", "dish", "dishes"
                            ]
                            if any(keyword in preprocess_query(query) for keyword in onam_sadhya_phrases):
                                response = knowledge_base["onam sadhya"]["responses"][language_preference]
                            else:
                                duration_phrases  = [
                                    "duration", "time", "fall", "onam celebrated", "thiruvonam",
                                    "days", "divasam", "divasangal", "day", "when", "epol", "epozh","month","masam","ennan"
                                ]
                                
                                if any(keyword in preprocess_query(query) for keyword in duration_phrases):
                                    response = knowledge_base["onam duration"]["responses"][language_preference]
                                else:
                                    matched_responses = []
                                    for question, data in knowledge_base.items():
                                        for q in data["questions"]:
                                            if preprocess_query(q) in query:
                                                matched_responses.append(data["responses"][language_preference])

                                    if matched_responses:
                                        response = random.choice(matched_responses)
                                    else:
                                        response = "Maveli: I'm sorry, I don't have the answer to that question."

    return response, language_preference




def main():
    user_name = greet_user()
    language_preference = "english"

    while True:
        user_input = input(f"{user_name}: ")  

        response, language_preference = handle_user_query(user_input, language_preference)
        speak_response(response, language_preference)

if __name__ == "__main__":
    main()
