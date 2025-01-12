import streamlit as st
from process_document import load_vectorstore, generate_suggestions
from components.chat import init_chat_state, display_messages, display_input_form
from components.suggestions import display_suggestions
from config.styles import CUSTOM_CSS


def main():
    st.set_page_config(page_title="Pharma Assistant", page_icon="💊", layout="centered")
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # Titolo principale
    st.markdown('<div class="title-button">💊 Pharma Assistant</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Il tuo assistente virtuale personalizzato</div>', unsafe_allow_html=True)

    # Inizializza lo stato della chat
    init_chat_state()
    vectorstore = load_vectorstore()
    if "suggested_questions" not in st.session_state:
        st.session_state.suggested_questions = generate_suggestions(vectorstore)

    # Mostra messaggi, suggerimenti e input form
    display_messages()
    display_suggestions(vectorstore, st.session_state.suggested_questions)
    display_input_form(vectorstore)

    st.markdown("""
       <footer>
           Questo assistente virtuale utilizza documentazione caricata per fornire risposte. Per domande specifiche, consulta un professionista.
       </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
