from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


def create_qa_chain():
    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(
        template="""Sei un assistente amichevole specializzato nei prodotti First Praedict.

        REGOLE DI COMPORTAMENTO:
        1. Per saluti come "ciao", "buongiorno", ecc., rispondi in modo cordiale e specifica che sei qui per aiutare con i prodotti First Praedict
        2. Per domande sui prodotti First Praedict, usa SOLO le informazioni nel contesto
        3. Per QUALSIASI altra domanda non relativa ai prodotti, rispondi SEMPRE e SOLO con:
           "Mi dispiace, posso rispondere solo a domande riguardanti i prodotti First Praedict e il loro utilizzo."
        4. Se la domanda riguarda i prodotti First Praedict ma l'informazione non è nel contesto, rispondi:
           "Non ho informazioni su questo aspetto specifico dei prodotti First Praedict nei documenti forniti."
        5. NON FORNIRE MAI informazioni generiche o di comune conoscenza

        Contesto sui prodotti First Praedict:
        {context}

        Domanda: {question}

        Prima di rispondere, verifica:
        - È un saluto? → Rispondi cordialmente specificando che sei qui per domande sui prodotti First Praedict
        - È una domanda sui prodotti? → Usa solo le informazioni del contesto
        - È altro? → Usa la risposta standard di limitazione al campo First Praedict

        Risposta:""",
        input_variables=["context", "question"]
    )
    return load_qa_chain(llm, chain_type="stuff", prompt=prompt)


def get_answer(vectorstore, question):
    try:
        # Check per i saluti
        greetings = ["ciao", "buongiorno", "buonasera", "salve", "hey", "hi", "hello"]
        if any(greeting in question.lower() for greeting in greetings):
            return "Ciao! Sono qui per aiutarti con qualsiasi domanda riguardante i prodotti First Praedict. Come posso assisterti oggi?"

        # Verifica se la domanda è potenzialmente relativa ai prodotti
        relevant_keywords = ["first praedict", "test", "prodotto", "kit", "vitamina", "ferro", "gravidanza"]
        is_potentially_relevant = any(keyword in question.lower() for keyword in relevant_keywords)

        if not is_potentially_relevant:
            return "Mi dispiace, posso rispondere solo a domande riguardanti i prodotti First Praedict e il loro utilizzo."

        retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        docs = retriever.get_relevant_documents(question)

        if not docs:
            return "Non ho informazioni su questo aspetto specifico dei prodotti First Praedict nei documenti forniti."

        chain = create_qa_chain()
        result = chain.invoke({"input_documents": docs, "question": question})
        return result["output_text"].strip()

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return "Mi dispiace, si è verificato un errore. Per favore, riprova con un'altra domanda."