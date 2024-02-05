import re
import spacy
import Longs

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define responses and patterns
responses = {
    "greeting": ["hello", "hi", "hey", "hi there", "howdy"],
    "ask_how_are_you": ["how are you?", "how are you doing?", "what's up?", "how's it going?"],
    "positive_response": ["I'm good, thank you!", "Feeling great, thanks for asking!", "Doing well, and you?"],
    "farewell": ["goodbye", "bye", "see you later", "take care"],
    "default_response": ["I'm not sure how to respond to that.", "Could you please rephrase that?",
                         "I didn't understand."]
}


# Function to check if a token is a verb
def is_verb(token):
    return token.pos_ == "VERB"


# Function to check if a token is a proper noun
def is_proper_noun(token):
    return token.pos_ == "PROPN"


# Function to check if a token is an auxiliary verb
def is_auxiliary(token):
    return token.dep_ == "aux"


# Function to check if a token is a personal pronoun
def is_personal_pronoun(token):
    return token.pos_ == "PRON" and token.dep_ == "nsubj"


# Function to check if a token is a question word
def is_question_word(token):
    return token.lower_ in ["who", "what", "when", "where", "why", "how"]


# Function to check if a token is a greeting
def is_greeting(token):
    return token.lower_ in ["hello", "hi", "hey"]


# Function to check if a token is a farewell
def is_farewell(token):
    return token.lower_ in ["goodbye", "bye"]


# Function to check all messages and determine the best response
def check_all_messages(message):
    doc = nlp(message)

    # Check for greetings and farewells
    for token in doc:
        if is_greeting(token):
            return "Hello!"
        elif is_farewell(token):
            return "Goodbye!"

    # Check for questions
    if any(is_question_word(token) for token in doc):
        return "I'm doing fine, thank you!"

    # Default response
    return "I'm not sure how to respond to that."


# Function to get responses based on user input
def get_responses(user_input):
    response = check_all_messages(user_input)
    return response


# Main chat function
def chat():
    print("Bot: Hi there! I'm a simple chatbot. You can start chatting with me.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        else:
            response = get_responses(user_input)
            print("Bot:", response)


if __name__ == "__main__":
    chat()
