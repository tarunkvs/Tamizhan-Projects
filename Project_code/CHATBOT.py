import nltk
nltk.download('punkt_tab')
import string
from nltk.tokenize import word_tokenize
responses = {
    "hello": "Hi there! How can I help you with Tamizhan Skills?",
    "hi": "Hello! Ask me anything about Tamizhan Skills.",
    "courses": "We offer courses in Python, Web Development, AI, and more.",
    "fees": "Most of our courses are free or come at a very low cost!",
    "location": "We are located in Tamil Nadu, India, but offer courses online.",
    "certificate": "Yes, we provide certificates after successful completion.",
    "internship": "We have internship opportunities through the National Internship Portal.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a great day!"
}
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]
    return tokens
def chatbot():
    print("Tamizhan Skills Chatbot\nType 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Thanks for chatting!")
            break

        tokens = preprocess(user_input)
        matched = False

        for word in tokens:
            if word in responses:
                print("Bot:", responses[word])
                matched = True
                break

        if not matched:
            print("Bot: I'm sorry, I don't understand. Try asking about courses, certificates, etc.")
if  __name__ == "__main__":
    chatbot()
