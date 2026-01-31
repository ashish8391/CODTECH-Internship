import nltk
import random
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read chatbot knowledge
with open("chatbot_data.txt", "r", errors="ignore") as file:
    data = file.read().lower()

sentences = data.split("\n")

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return " ".join(tokens)

processed_sentences = [preprocess(sentence) for sentence in sentences]

def chatbot_response(user_input):
    user_input = preprocess(user_input)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(processed_sentences + [user_input])
    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    idx = similarity.argmax()

    if similarity[0][idx] == 0:
        return "Sorry, I don't understand."
    else:
        return sentences[idx + 1]

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    if user.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user))
