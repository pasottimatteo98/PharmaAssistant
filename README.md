# Pharma Assistant

**Pharma Assistant** è un'applicazione interattiva in TEST per fornire assistenza virtuale. Questa applicazione utilizza documenti di riferimento per rispondere a domande specifiche sui prodotti e il loro utilizzo.

## Funzionalità

- Interfaccia utente interattiva con design personalizzato.
- Utilizzo di documenti (Word, PDF, TXT) come riferimento per il chatbot.
- Utilizzo di FAISS e modelli OpenAI per rispondere a domande basate sui documenti caricati.
- Risposte accurate basate esclusivamente sulle informazioni disponibili nei documenti forniti.

## Requisiti

Prima di iniziare, assicurati di avere i seguenti requisiti installati sul tuo sistema:

- Python 3.8 o superiore
- Librerie specificate nel file `requirements.txt`

## Installazione

1. Clona il repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
   
Installa le dipendenze:
  ```bash
  pip install -r requirements.txt
  ```

Crea un file .env nella directory principale e aggiungi la tua chiave API OpenAI:

```bash
OPENAI_API_KEY=your_api_key_here
```
Assicurati che il documento di riferimento (Sito_First_Praedict.docx) sia presente nella directory radice.

Esecuzione
Crea l'indice FAISS utilizzando il comando:

```bash
Copia codice
python process_document.py
```
Avvia l'applicazione:

```bash
streamlit run app.py
```
Apri il tuo browser e accedi all'applicazione su http://localhost:8501.

## Architettura del Progetto

- **`app.py`**: File principale per l'interfaccia utente di Streamlit.
- **`process_document.py`**: Script per creare e gestire l'indice FAISS.
- **`requirements.txt`**: File contenente le dipendenze del progetto.
- **`Sito_First_Praedict.docx`**: Documento di riferimento per il chatbot.

## Limitazioni

- L'assistente risponde solo a domande riguardanti i prodotti **First Praedict** e il loro utilizzo.
- Le informazioni sono basate esclusivamente sui documenti caricati.
- Non vengono aggiunte informazioni esterne.


