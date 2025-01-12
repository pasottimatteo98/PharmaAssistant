import streamlit as st
from utils.chat_logic import process_message

def init_chat_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        st.session_state.show_welcome = True
        st.session_state.show_suggestions = True
        st.session_state.first_interaction = True

def display_messages():
    chat_container = st.container()
    with chat_container:
        if st.session_state.show_welcome:
            st.markdown(
                f'<div class="chat-message bot-message">Ciao! Sono qui per aiutarti. Come posso assisterti oggi?</div>',
                unsafe_allow_html=True)

        for message in st.session_state.messages:
            div_class = "chat-message user-message" if message["role"] == "user" else "chat-message bot-message"
            st.markdown(f'<div class="{div_class}">{message["content"]}</div>', unsafe_allow_html=True)



def display_input_form(vectorstore):
    st.session_state.vectorstore = vectorstore

    with st.form("chat_input", clear_on_submit=True):
        cols = st.columns([8, 2])
        with cols[0]:
            placeholder_text = "Come posso aiutarti?" if st.session_state.first_interaction else ""
            user_input = st.text_input(
                "Scrivi la tua domanda:",
                placeholder=placeholder_text,
                label_visibility="collapsed",
                key="user_input"
            )
        with cols[1]:
            submitted = st.form_submit_button("Invia", use_container_width=True)
            if submitted and user_input:
                process_message(user_input, vectorstore)
                st.rerun()
