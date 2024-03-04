from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
load_dotenv()

def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents


def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs


def similarity_search(docs, query):
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embeddings)
    matching_docs = db.similarity_search(query)
    return matching_docs


def run_qa_chain(docs, query):
    model_name = "gpt-3.5-turbo"
    llm = ChatOpenAI(model_name=model_name)
    chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
    answer = chain.run(input_documents=docs, question=query)
    return answer


def process_qa(query, docs):
    matching_docs = similarity_search(docs, query)
    prompt = f"""
        Com base nesse contexto {matching_docs} verifique se há possibilidade de recomendar algum outro produto para a solicitação a seguir: {query}, se não houver ignore a sugestão e apenas responda de acordo com a solicitação.
    """
    answer = run_qa_chain(matching_docs, prompt)
    return answer
