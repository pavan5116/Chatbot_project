import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAI as ai

# Set up API key securely
os.environ["GOOGLE_API_KEY"] = "Your-Google-api-key"

# Initialize LLM
llm = ai(temperature=0, model="gemini-2.0-flash")

# Streamlit UI
st.title("AI Chatbot")

user_prompt = st.text_input("Enter your prompt:")
if user_prompt:
    response = llm.invoke(user_prompt) 
    st.write("***Chatbot:***", response)


