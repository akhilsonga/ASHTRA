import streamlit as st
from dataclasses import dataclass
import sys
import os
sys.path.append('D:/Kotta/Lablab/pages/RAG')
print(sys.path)
from RAG import RAG,RAG_query
print(os.getcwd())
if 'sidebar_state' not in st.session_state:
        st.session_state.sidebar_state = 'collapsed'
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)
# parser("./2305.05176.pdf")

# Function to process chat input (decorated with st.cache)
@st.cache_data
def process_chat_input(chat_message):
    response = RAG_query(chat_message)
    return response

# Dataclass for message
@dataclass
class Message:
    actor: str
    payload: str

def main():
    USER = "user"
    ASSISTANT = "ai"
    MESSAGES = "messages"
    PLAY_AUDIO = "play_audio"

    # Initialize messages if not in session state
    
    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi! How can I help you?")]

    # Initialize audio state
    if PLAY_AUDIO not in st.session_state:
        st.session_state[PLAY_AUDIO] = False

    # Render existing messages
    for msg in st.session_state[MESSAGES]:
        st.chat_message(msg.actor).write(msg.payload)

    # Audio player (only if PLAY_AUDIO is True)
    if st.session_state[PLAY_AUDIO]:
        st.sidebar.image('thumbnail1.jpg', use_column_width=True)
        st.sidebar.audio('http://127.0.0.1:5000/stream', format='audio/mp3')

    # Chat input and processing
    prompt = st.chat_input("Ask a question!")

    if prompt:
        st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
        st.chat_message(USER).write(prompt)

        # Process user input
        response = process_chat_input(prompt)

        # Add response to messages
        st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
        st.chat_message(ASSISTANT).write(response)
        st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'expanded' else 'collapsed'

    if st.button("Listen", key="listen_button"):
        st.session_state[PLAY_AUDIO] = True
        st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
if __name__ == "__main__":
    # print(st.session_state.sidebar_state)
    st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: max !important; /* Set the width to your desired value */
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
        #listen_button {
            width: max
        }
    </style>
        """, unsafe_allow_html=True,
    )

    main()
