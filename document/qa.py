from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


def create_qa_chain():
    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(
        template="""Sei un assistente amichevole ed esperto dei prodotti First Praedict. 
        Rispondi in modo naturale alle interazioni, ma per informazioni sui prodotti usa SOLO le informazioni fornite nel seguente contesto.
        Se l'informazione richiesta non è presente nel contesto, rispondi SEMPRE con:
        "Non ho informazioni su questo aspetto nei documenti forniti."

        Se la domanda è al di fuori dell'ambito dei prodotti First Praedict o dei loro usi, rispondi:
        "Posso rispondere solo a domande riguardanti i prodotti First Praedict e il loro utilizzo."

        Contesto:
        {context}

        Domanda: {question}

        Risposta:""",
        input_variables=["context", "question"]
    )
    return load_qa_chain(llm, chain_type="stuff", prompt=prompt)


def get_answer(vectorstore, question):
    try:
        retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        docs = retriever.get_relevant_documents(question)

        if not docs:
            return "Non ho informazioni su questo argomento nei documenti forniti."

        chain = create_qa_chain()
        result = chain.invoke({"input_documents": docs, "question": question})
        return result["output_text"].strip()

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")
        return "Mi dispiace, si è verificato un errore. Per favore, riprova con un'altra domanda."