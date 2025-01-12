CUSTOM_CSS = """
<style>
/* Importazione del font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

/* Stile generale dell'app */
div.stApp {
    background-color: #f8fafc;
    font-family: 'Inter', sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 1rem;
}

/* Trasforma il bottone reset in un titolo */
div.stButton > button#reset_chat {
    background: none !important;
    border: none !important;
    padding: 0 !important;
    color: #0d7490 !important;
    font-size: 3.2rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    height: auto !important;
    display: flex !important;
    box-shadow: none !important;
    outline: none !important;
    justify-content: center !important;
    align-items: center !important;
    margin: 0 auto 0.5rem !important;
    transition: transform 0.2s ease-in-out !important;
    text-align: center !important;
}

/* Container del bottone titolo */
div.stButton {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
}

div.stButton > button#reset_chat:hover {
    color: #1d9fbf !important;
    transform: scale(1.02);
}

/* Sottotitolo */
div.subtitle {
    color: #64748b;
    text-align: center;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Stile dei suggerimenti */
div.stButton > button {
    background-color: white !important;
    color: #334155 !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
    height: auto !important;
    font-size: 1rem !important;
    line-height: 1.5 !important;
    transition: all 0.2s ease-in-out !important;
    margin-bottom: 0.75rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}

/* Hover dei suggerimenti */
div.stButton > button:hover {
    background-color: #f8fafc !important;
    border-color: #cbd5e1 !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
}

/* Messaggi nella chat */
div.chat-message {
    padding: 1rem 1.25rem;
    border-radius: 12px;
    margin: 8px 0;
    max-width: 85%;
    line-height: 1.5;
}

/* Messaggi utente */
div.user-message {
    background-color: #0d7490;
    color: white;
    margin-left: auto;
    border-radius: 12px 12px 0 12px;
}

/* Messaggi del bot */
div.bot-message {
    background-color: #f1f5f9;
    color: #334155;
    margin-right: auto;
    border-radius: 12px 12px 12px 0;
}

/* Input di testo */
div.stTextInput > div > div {
    border-radius: 12px;
}

/* Pulsante invio nei form */
button[kind="primaryFormSubmit"] {
    border-radius: 12px !important;
    background-color: #0d7490 !important;
    height: 45px !important;
}

/* Contenitore dei form */
div[data-testid="stForm"] {
    border: none;
    padding: 0;
}

.title-button {
    all: unset;
    display: block;
    width: 100%;
    font-family: 'Inter', sans-serif;
    font-size: 3.2rem;
    font-weight: 700;
    color: #0d7490;
    text-align: center;
    cursor: pointer;
    background: none;
    border: none;
    padding: 1.5rem 0;
    margin: 0;
    line-height: 1.2;
    transition: color 0.2s ease-in-out;
}

.title-button:hover {
    color: #1d9fbf;
}

/* Per rimuovere l'outline quando il bottone è in focus */
.title-button:focus {
    outline: none;
}




/* Footer */
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(255,255,255,0.9);
    backdrop-filter: blur(10px);
    padding: 0.75rem;
    text-align: center;
    font-size: 0.8rem;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    z-index: 999;
}
</style>
"""