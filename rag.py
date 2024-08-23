import streamlit as st
import json
import numpy as np
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.docstore.document import Document

key='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'

# load file
# Load your JSON file
def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# Convert JSON to Document format
def json_to_doc(data):
    documents = [
        Document(
            page_content=entry['question'],  # The question becomes the page content
            metadata={
                "answer": entry['answer'],  # The answer is stored in metadata
                "location": entry.get("location", None)  # The location is also stored in metadata, if it exists
            }
        )
        for entry in data
    ]
    return documents

def get_vectorstore(documents):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key= key)
    vectorstore = FAISS.from_documents(documents,embedding=embeddings)
    return vectorstore

def handle_userinput(user_question):
    if "vectorstore" in st.session_state and st.session_state.vectorstore:
        results = st.session_state.vectorstore.similarity_search_with_score(
            user_question,
            k=2,
        )
        threshold=1
        output='==> '
        for res in results:
            # Check if the distance between the query and best match is less than the threshold
            if  res[1] <= threshold:
                for elem in res[0].metadata['answer']:
                    if  res[0].metadata['location']!=None and res[0].metadata['location']!='unknown':
                        output= output+ elem+'-'+ res[0].metadata['location'] +'\n\n==> '
                    else:
                        output = output + elem+'\n\n==> '
            else:
                continue
        if output=='==> ':
            output='I have no recommendations. What kind of restaurant are you looking for?'
        else:
            output= output[:len(output)-4]
        st.session_state.messages.append({"role": "assistant", "content": output})
    else:
        st.warning("Please process the PDF documents first.")


def main():
   
    st.set_page_config(page_title='Restaurant Recommendation Bot')
    

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.header('Restaurant Recommendation Bot 🍽️')
    user_question = st.chat_input("Ask a question:")

    data=read_json('/combined_file.json')
    #st.write(data)
    docs= json_to_doc(data)
    st.session_state.vectorstore = get_vectorstore(docs)
    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})
        handle_userinput(user_question)

    

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


if __name__ == '__main__':
    main()