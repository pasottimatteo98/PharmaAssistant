import streamlit as st
from process_document import load_vectorstore, chatbot_query

# Configurazione della pagina
st.set_page_config(
    page_title="Pharma Assistant",
    page_icon="💊",
    layout="centered"
)

# Stile CSS personalizzato
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f4f9;
        font-family: 'Arial', sans-serif;
    }
    .chat-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .user-message {
        background-color: #00796b;  /* Verde intenso */
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 10px 0;
        max-width: 75%;
        float: right;
        clear: both;
    }
    .bot-message {
        background-color: #dcedc8;  /* Verde chiaro */
        color: #33691e;  /* Verde scuro */
        padding: 10px 15px;
        border-radius: 15px;
        margin: 10px 0;
        max-width: 75%;
        float: left;
        clear: both;
    }
    .main-title {
        color: #00796b;
        text-align: center;
        padding: 30px 10px;
        font-size: 2.5em;
        font-weight: bold;
    }
    .subtitle {
        color: #4f4f4f;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: #00796b;
        color: white;
        border: none;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #004d40;
    }
    </style>
    """, unsafe_allow_html=True)

# Area principale
st.markdown('<div class="main-title">💊 Pharma Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Il tuo assistente virtuale personalizzato</div>', unsafe_allow_html=True)

# Inizializza la sessione
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ciao! Sono qui per aiutarti. Come posso assisterti oggi?"}
    ]

# Carica il vectorstore
try:
    vectorstore = load_vectorstore()
except:
    st.warning("⚠️ Nessun documento di riferimento disponibile. Il bot potrebbe non essere in grado di rispondere.")
    vectorstore = None

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        div_class = "user-message" if message["role"] == "user" else "bot-message"
        st.markdown(f'<div class="{div_class}">{message["content"]}</div>', unsafe_allow_html=True)

# Chat input
with st.container():
    st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True)  # Spacing
    with st.form("chat_input", clear_on_submit=True):
        cols = st.columns([8, 2])
        with cols[0]:
            user_input = st.text_input(
                "Scrivi la tua domanda:",
                placeholder="Come posso aiutarti?",
                label_visibility="collapsed"
            )
        with cols[1]:
            submit_button = st.form_submit_button("Invia", use_container_width=True)

        if submit_button and user_input:
            if not vectorstore:
                st.error("⚠️ Impossibile processare la richiesta: nessun documento di riferimento disponibile.")
            else:
                # Aggiungi messaggio utente
                st.session_state.messages.append({"role": "user", "content": user_input})

                # Ottieni risposta
                response = chatbot_query(vectorstore, user_input)

                # Aggiungi risposta bot
                st.session_state.messages.append({"role": "assistant", "content": response})

                # Ricarica
                st.rerun()

# Footer
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: white; padding: 15px; text-align: center; font-size: 0.85em; color: #4f4f4f; border-top: 1px solid #ddd;">
        Questo assistente virtuale utilizza documentazione caricata per fornire risposte. Per domande specifiche, consulta un professionista.
    </div>
    """, unsafe_allow_html=True)
