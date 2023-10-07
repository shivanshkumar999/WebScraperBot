from hugchat import hugchat
from hugchat.login import Login
import requests
from bs4 import BeautifulSoup
import time
import sys

from flask import Flask, render_template, request, jsonify

sign = Login("shivanshkumar752@gmail.com", "James.bond.990")
cookies = sign.login()

cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

# Typewriter effect
def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)
    time.sleep(1)


# A function to take user input
# def takechoice() -> int:
#     choice = input("What do you want?\n1. Web Scrape Data using the bot?\n2. Interact with the bot to check it's capabilities.\nEnter input : ")
#     return choice

# A function to scrape data, easy and simple
def scrapper():
    output=[]
    close=["close","no","bye","off"]
    print("\n_______________________________________________\n")
    link = input("Enter the website you want to scrape (Note that some websites may block web scraping, so the results may be inadequate or unexpected) : ")
    if link not in close:
        try:
            typewriter_effect("Wait Scraping Data and giving a sensible response to you.")
            r = requests.get(link)
            soup = BeautifulSoup(r.content, "html.parser")
            for div in soup.find_all("p"):
                # print(div.get_text())
                output.append(div.get_text())
            output = "".join(output)
            query = "give a sensible and meaningful interpretation of this web scraped output of a website and even explain it to user, you as first person and user as second person: " + output
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            query_result = chatbot.query(query, web_search=True)
            if query_result:
                print("\n")
                typewriter_effect(f"{query_result}")
            print("\n_______________________________________________\n")
            querysimulator("Ask me if I have any more questions?")
        
        except Exception as error:
            print("\n")
            typewriter_effect(f"Sorry, The scraping could not be performed because of this error :  {error}. Kindly, enter the correct url again.")
            scrapper()
    else:
        querysimulator("Ask me if I have any more questions?")

    print("\n_______________________________________________\n")

# A program for bot
# Enter the dedicated command "PWS" to perform web scrapping. Else the bot would interpret the output in a different way and would
# give the response

# Since the bot is a GEN AI model, it would give an answer to even a wrong query also.

def querysimulator(query):
    close=["close","no","bye","off"]
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    query_result = chatbot.query(query, web_search=True)
    typewriter_effect(f"Bot : {query_result}")
    if query_result:
        print("\n_______________________________________________\n")
        query = input("You : ")
        query = query.lower()
        if query in close:
            typewriter_effect("Bot : Thanks for using the bot! GoodBye and Have a Nice Day")
        elif query == "pws":
            scrapper()
        else:
            querysimulator(query)
            print("\n_______________________________________________\n")



querysimulator("Hi!")


# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_input = request.form['user_input']
#         response = querysimulator(user_input)
#         return jsonify({'response': response})
#     return render_template('index.html')

# # Rest of your code here...

# if __name__ == '__main__':
#     app.run(debug=True)