# chatbot_app/views.py

import nltk
import spacy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from nltk.chat.util import Chat, reflections

# Download required NLTK data files
nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

# Define chatbot pairs
pairs = [
    ["hi|hello|hey", ["Hello! How can I help you today?", "Hi there!"]],
    ["how are you?", ["I'm a bot, but thanks for asking! How can I assist you?"]],
    ["what is your name?", ["I'm your helpful chatbot!", "I don't have a name, but I'm here to help you."]],
    ["(.*) help (.*)", ["I'm here to help! Tell me more about what you need."]],
    ["(.*) weather (.*)", ["I'm unable to check the weather, but you can try a weather app or site!"]],
    ["(.*) your (age|creator|purpose)?", ["I was created by a developer to assist you!"]],
    ["bye|exit|quit", ["Goodbye! Have a great day!", "See you next time!"]],
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(text):
    doc = nlp(text.lower())
    response = chatbot.respond(text)
    if response is None:
        return "I'm not sure I understand. Can you tell me more?"
    return response

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response_text = chatbot_response(user_message)
        return JsonResponse({'response': response_text})


# Add this function to views.py

from django.shortcuts import render

def chat_view(request):
    return render(request, "chatbot_app/chat.html")
