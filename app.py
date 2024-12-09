import json
import random
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


with open("intent.json", "r") as file:
    data = json.load(file)


intents = data["intents"]
intent_texts = {intent["intent"]: intent["text"] for intent in intents}
intent_responses = {intent["intent"]: intent["responses"] for intent in intents}


all_texts = []
intent_map = []  
for intent, texts in intent_texts.items():
    all_texts.extend(texts)
    intent_map.extend([intent] * len(texts))


vectorizer = CountVectorizer().fit(all_texts)
text_vectors = vectorizer.transform(all_texts)

def preprocess_text(text):
    text = text.lower()
    return text


def get_intent(user_input):
    user_input = preprocess_text(user_input)
    user_vector = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_vector, text_vectors)
    best_match_idx = np.argmax(similarity_scores)
    confidence = similarity_scores[0, best_match_idx]
    
    if confidence > 0.3:  
        return intent_map[best_match_idx]
    return None


def get_response(intent):
    if intent in intent_responses:
        return random.choice(intent_responses[intent])
    return "I'm sorry, I don't understand that."


st.title("Chatbot using NLP")
st.write("This is a simple chatbot. Type your message below!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(f"You: {user_input}")
        intent = get_intent(user_input)
        if intent:
            response = get_response(intent)
        else:
            response = "I'm sorry, I don't understand that."
        st.session_state.chat_history.append(f"Chatbot: {response}")


for message in st.session_state.chat_history:
    st.write(message)
