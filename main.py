#HELP BOT FOR DECATHLON
#Named as decpy

import datetime
import webbrowser
import openai
import speech_recognition as sr
import win32com.client
import os
from config import apikey
import random

chatbot=" "
def chat(query):
    global chatbot
    print(chatbot)

    openai.api_key = apikey
    chatbot+="Helper:{ptompt}\n Jarvis:";

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatbot,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response['choices'][0]['text'])
    chatbot+= f"{response['choices'][0]['text']}\n"
    return  response["choices"][0]["text"]
def ai(prompt):
    openai.api_key = apikey
    testseries=f"{prompt}\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response['choices'][0]["text"])
    testseries+=response['choices'][0]["text"]

    if not os.path.exits("openai"):
        os.mkdir("openai")

    with open(f"openai/prompt-{random.randint(1,245242331)}","w") as f:
        f.write(testseries)

speaker =win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.4
        audio = r.listen(source)

        try:
            print("Recognizing..............................")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said{query}")
            return query

        except Exception as e:
            return "Some error occured, from myside"
def say(text):
    speaker.Speak(text)

if __name__ == '__main__':

    print('Welcome aboard to Decathlon Help services')
    print("THis Decpy, the Virtual Assistant of decathlon")
    while True:
        print("Decpy ,listening................")
        query = takeCommand()

        #todo:Add more sites
        sites =[["youtube","https://www.youtube.com/"],["times of india","https://timesofindia.indiatimes.com/?from=md"],["youtube","https://www.youtube.com/"],["google","https://www.google.com/"]]

        for site in sites:
            if f"open{site[0]}".lower() in query.lower():
                say(f"Opening{site[0]}  sir")
                webbrowser.open(site[1])

    #todo:Add a any feature within this you want to execute on command

        if "decpy ,what is the time" in query:
            strfTime =datetime.datetime.now().strftime("%H:%M::%S")
            print(say(f"Sir\mam The time is {strfTime}"))

        if "google chrome".lower() in query.lower():
            #todo:type the paticualar file location here which you want access
            os.system("_______________________________")

        if "Decpy".lower() in query.lower():
            ai(prompt=query)

        elif "Decpy quit".lower() in query.lower():
            exit()

        elif "Reset".lower() in query.lower():
            chatbot=" "
        else:
            print("Decpy Assisting")
            chat(query)