import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the key from environment
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.divider()

displaytext= ('''## About somaGPT ''')

st.markdown(displaytext)

displaytext= (
    '''SomaGPT is a platform for learning programming in a socratic manner. \n\n'''
    '''It uses foundational LLMS such as GPT and Gemini. '''
    '''Instead of the LLM giving you answers it instructs you in an adaptive way by leveraging on your prior knowledge \n\n'''

 )
st.divider()
st.markdown(displaytext)

st.title("OOP programming instructor")
st.write("I am glad you want to learn the object oriented concepts. They are a key conecpt in programming. Mastering this will move you from to an advanced programmer. Tell me what topic you want to learn about classes and objects")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["parts"][0])

# User input
user_input = st.chat_input("Say something")

if user_input:
    # Append user message using correct Gemini format
    st.session_state.chat_history.append({
        "role": "user",
        "parts": [user_input]
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Debug: Check the chat history before sending to Gemini
    #st.write("Chat History Sent to Model:", st.session_state.chat_history)

    try:
        # Generate response with full chat history
        response = model.generate_content(st.session_state.chat_history)
        bot_reply = response.text

        # Check if the response is generated
        if bot_reply:
            # Append model response using correct Gemini format
            st.session_state.chat_history.append({
                "role": "model",
                "parts": [bot_reply]
            })

            with st.chat_message("model"):
                st.markdown(bot_reply)
        else:
            st.error("No response generated. Check API settings.")
    except Exception as e:
        st.error(f"Error generating response: {e}")