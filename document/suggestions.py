from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from operator import itemgetter


def generate_suggestions(vectorstore):
    prompt = """Analizza il contenuto e genera 6 domande frequenti pertinenti sui prodotti First Praedict.
    Le domande devono essere brevi, chiare e coprire aspetti diversi dei prodotti.
    Restituisci solo l'elenco delle domande, una per riga."""

    try:
        llm = OpenAI(temperature=0.2)
        docs = vectorstore.similarity_search(prompt, k=4)
        context = "\n".join([doc.page_content for doc in docs])

        template = """{context}\n\nGenera domande basate su questo contesto:\n{question}"""
        prompt_template = PromptTemplate(template=template, input_variables=["context", "question"])

        chain = (
                RunnableParallel(
                    context=RunnablePassthrough(),
                    question=lambda x: prompt
                )
                | prompt_template
                | llm
        )

        result = chain.invoke(context)
        questions = [q.strip() for q in result.split("\n") if q.strip()]
        return questions[:6]

    except Exception as e:
        print(f"Errore generazione suggerimenti: {str(e)}")
        return [
            "Come funziona il test di gravidanza?",
            "Quando effettuare il test di vitamina D?",
            "Come si usa il test del ferro?",
            "Come interpretare i risultati?",
            "Quali sono le precauzioni d'uso?",
            "Come conservare i test?"
        ]