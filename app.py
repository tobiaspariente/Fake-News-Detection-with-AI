import streamlit as st
import pickle
from token_go import clean_and_tokenize
import numpy as np

def preprocessor(text):
    return text

def tokenizer(text):
    return text

# Load the trained model
with open('final_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app interface
st.title("Fake News Detection")

# Take user input (news article)
user_input = st.text_area("Enter the news article here:")

if st.button("Predict"):
    if user_input:
        # Clean and tokenize the input text
        tokenized_input = clean_and_tokenize(user_input)
        
        # Predict using the model
        prediction = model.predict([tokenized_input])
        
        # Display the result
        if prediction[0] == 0:
            st.write("This is Fake News!")
        else:
            st.write("This is Real News!")
    else:
        st.write("Please enter some text!")

# run this in a terminal
# streamlit run /Users/tobiaspariente/Desktop/PYTHON/PHASE_5/app.py