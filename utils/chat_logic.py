import streamlit as st
from process_document import chatbot_query
import time


def process_message(message, vectorstore):
    # Aggiungi subito il messaggio dell'utente alla sessione
    st.session_state.messages.append({"role": "user", "content": message})
    st.session_state.first_interaction = False

    # Aggiungi un placeholder per la risposta del bot
    st.session_state.messages.append({"role": "assistant", "content": "In elaborazione..."})

    # Calcola la risposta
    try:
        response = chatbot_query(vectorstore, message)
        # Sostituisci il placeholder con la risposta effettiva
        st.session_state.messages[-1]["content"] = response
        st.session_state.show_suggestions = False
    except Exception as e:
        # Sostituisci il placeholder con un messaggio di errore
        st.session_state.messages[-1]["content"] = f"Errore: {str(e)}"

        # Rerun per mostrare immediatamente il messaggio dell'utente
        st.rerun()
