import streamlit as st
from utils.chat_logic import process_message

def display_suggestions(vectorstore, suggested_questions):
    if st.session_state.get("show_suggestions", True):
        st.markdown('<div class="suggestions-title">Domande frequenti:</div>', unsafe_allow_html=True)
        for i, question in enumerate(suggested_questions):
            if st.button(question, key=f"suggestion_{i}", use_container_width=True):
                process_message(question, vectorstore)
                st.rerun()  # Forza l'aggiornamento immediato
