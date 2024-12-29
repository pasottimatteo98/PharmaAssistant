from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()

# Legge la chiave API da .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("La chiave API OPENAI_API_KEY non è definita nel file .env")

os.environ["OPENAI_API_KEY"] = api_key



def create_faiss_index(docx_path, index_path="faiss_index"):
    loader = UnstructuredWordDocumentLoader(docx_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
    )
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)
    print("Indice FAISS creato e salvato.")


def load_vectorstore(index_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)


def chatbot_query(vectorstore, question):
    try:
        # Configurazione del retriever
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        # Recupero dei documenti
        docs = retriever.get_relevant_documents(question)
        if not docs:
            return "Non ho informazioni su questo argomento nei documenti forniti."

        # Preparazione del contesto combinando i documenti
        context = "\n\n".join([doc.page_content for doc in docs])

        # Configurazione LLM
        llm = OpenAI(temperature=0)

        # Prompt template
        prompt = PromptTemplate(
            template="""Sei un assistente che risponde SOLO ed ESCLUSIVAMENTE utilizzando le informazioni fornite nel seguente contesto. 
            Non aggiungere MAI informazioni esterne o supposizioni.
            Se l'informazione richiesta non è presente nel contesto, rispondi SEMPRE con:
            "Non ho informazioni su questo aspetto nei documenti forniti."

            Se la domanda è al di fuori dell'ambito dei prodotti First Praedict o dei loro usi, rispondi:
            "Posso rispondere solo a domande riguardanti i prodotti First Praedict e il loro utilizzo."

            Contesto:
            {context}

            Domanda: {question}

            Risposta (usa SOLO le informazioni dal contesto fornito):""",
            input_variables=["context", "question"]
        )

        # Creazione della chain
        chain = load_qa_chain(
            llm,
            chain_type="stuff",
            prompt=prompt
        )

        # Esecuzione della query
        result = chain({"input_documents": docs, "question": question})

        return result["output_text"].strip()

    except Exception as e:
        print(f"Errore dettagliato: {str(e)}")  # Logging dettagliato dell'errore
        return "Mi dispiace, si è verificato un errore. Per favore, riprova con un'altra domanda."


if __name__ == "__main__":
    create_faiss_index("Sito_First_Praedict.docx")