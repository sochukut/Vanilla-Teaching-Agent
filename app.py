import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets
api_key = st.secrets["api_keys"]["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Page layout
st.divider()
st.markdown("## About somaGPT")
st.write(
    "SomaGPT is a platform for learning programming in a Socratic manner. It uses foundational LLMs such as GPT and Gemini.
    Instead of the LLM giving you answers, it instructs you in an adaptive way by leveraging your prior knowledge."
)
st.divider()
st.title("OOP Programming Instructor")
st.write(
    "I’m glad you want to learn object-oriented concepts. They’re key in programming.\n"
    "Mastering them will help you become an advanced programmer.\n"
    "Tell me what topic you want to learn about classes and objects."
)

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# User input box
user_input = st.chat_input("Ask me anything about OOP...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Get response from Gemini
        response = st.session_state.chat.send_message(user_input)
        bot_reply = response.text

        if bot_reply:
            with st.chat_message("model"):
                st.markdown(bot_reply)
        else:
            st.error("Gemini returned no response.")
    except Exception as e:
        st.error(f"Error generating response: {e}")
