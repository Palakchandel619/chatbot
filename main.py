import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("Chatbot_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title="AI Chatbot",page_icon="😑",layout="centered")
st.title("AI Chatbot")
st.write("Chat With Gemini")
if "messages" not in st.session_state:
    st.session_state.messages=[]    
for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.markdown(message["content"])
user_input = st.chat_input("Type your message... ")

if user_input:

    # show user input
    st.chat_message("user").markdown(user_input)

    # Save user input
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })
    response = model.generate_content(user_input)

    ai_response = response.text

    # show ai response
    st.chat_message("assistant").markdown(ai_response)
    
    # Save AI response
    st.session_state.messages.append({
        "role":"assistant",
        "content":ai_response
    })