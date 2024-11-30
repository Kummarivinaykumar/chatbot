import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Download required NLTK data files
nltk.download('punkt')

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define sample patterns and responses
pairs = [
    ["hi|hello|hey", ["Hello! How can I help you today?", "Hi there!"]],
    ["how are you?", ["I'm a bot, but thanks for asking! How can I assist you?"]],
    ["what is your name?", ["I'm your helpful chatbot!", "I don't have a name, but I'm here to help you."]],
    ["(.*) help (.*)", ["I'm here to help! Tell me more about what you need."]],
    ["(.*) weather (.*)", ["I'm unable to check the weather, but you can try a weather app or site!"]],
    ["(.*) your (age|creator|purpose)?", ["I was created by a developer to assist you!"]],
    ["bye|exit|quit", ["Goodbye! Have a great day!", "See you next time!"]],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Define a function to process and respond to user input
def chatbot_response(text):
    doc = nlp(text.lower())
    # Simple fallback if no patterns match
    response = chatbot.respond(text)
    if response is None:
        return "I'm not sure I understand. Can you tell me more?"
    return response


# Run the chatbot loop
def chat():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        print("Chatbot:", chatbot_response(user_input))

# Start the chatbot
chat()
