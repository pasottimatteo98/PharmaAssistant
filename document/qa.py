from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


def create_qa_chain():
    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(
        template="""Sei un assistente amichevole specializzato nei prodotti e nelle informazioni First Praedict.

        REGOLE DI COMPORTAMENTO:
        1. Se la domanda è un semplice saluto SENZA altre domande (es. solo "ciao", "buongiorno"), rispondi in modo cordiale
        2. Se la domanda contiene un saluto MA anche una richiesta di informazioni, rispondi alla richiesta di informazioni
        3. Per le domande, usa SOLO le informazioni nel contesto fornito
        4. Se l'informazione richiesta non è presente nel contesto, rispondi:
           "Non ho informazioni su questo aspetto specifico nei documenti First Praedict forniti."
        5. Cerca di fornire risposte complete e dettagliate quando le informazioni sono disponibili nel contesto
        6. Se trovi qualche abbreviazione non presente nel documento, espandila e cercala nuovamente

        Contesto First Praedict:
        {context}

        Domanda: {question}

        Prima di rispondere:
        - È solo un saluto senza domande? → Rispondi cordialmente
        - È una domanda con informazioni nel contesto? → Fornisci una risposta completa
        - L'informazione non è nel contesto? → Usa la risposta standard di mancanza informazioni

        Risposta:""",
        input_variables=["context", "question"]
    )
    return load_qa_chain(llm, chain_type="stuff", prompt=prompt)

def get_answer(vectorstore, question):
    try:
        # Check per i saluti semplici senza altre domande
        greetings = ["ciao", "buongiorno", "buonasera", "salve", "hey", "hi", "hello"]
        if question.lower() in greetings:
            return "Ciao! Sono qui per aiutarti con qualsiasi domanda riguardante i prodotti e le informazioni First Praedict. Come posso assisterti oggi?"

        # Cerchiamo documenti rilevanti per la domanda
        retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        docs = retriever.get_relevant_documents(question)

        # Se troviamo documenti rilevanti, procediamo con la risposta
        if docs:
            chain = create_qa_chain()
            result = chain.invoke({"input_documents": docs, "question": question})
            return result["output_text"].strip()

        # Se non troviamo documenti rilevanti
        return "Non ho informazioni su questo aspetto specifico nei documenti First Praedict forniti."

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return "Mi dispiace, si è verificato un errore. Per favore, riprova con un'altra domanda."