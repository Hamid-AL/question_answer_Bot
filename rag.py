import streamlit as st
import json
from langchain_community.embeddings.openai import OpenAIEmbeddings  # Updated to langchain_openai
from langchain_community.vectorstores import FAISS  # Updated to langchain_community
from langchain_community.docstore.document import Document

key = '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'



# Load JSON file
@st.cache_data
def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Convert JSON to Document format
def json_to_doc(data):
    documents = [
        Document(
            page_content=entry['question'],
            metadata={
                "answer": entry['answer'],
                "location": entry.get("location", None)
            }
        )
        for entry in data
    ]
    return documents

# Initialize FAISS with GPU support
@st.cache_resource
def get_vectorstore(_documents):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key= key)
    vectorstore = FAISS.from_documents(_documents,embedding=embeddings)
    return vectorstore

# Handle user input
def handle_userinput(user_question):
    if "vectorstore" in st.session_state and st.session_state.vectorstore:
        results = st.session_state.vectorstore.similarity_search_with_score(user_question, k=2)
        threshold = 1
        output = '==> '
        for res in results:
            if res[1] <= threshold:
                for elem in res[0].metadata['answer']:
                    if res[0].metadata['location'] != None and res[0].metadata['location'] != 'unknown':
                        output = output + elem + '-' + res[0].metadata['location'] + '\n\n==> '
                    else:
                        output = output + elem + '\n\n==> '
            else:
                continue
        if output == '==> ':
            output = 'I have no recommendations. What kind of restaurant are you looking for?'
        else:
            output = output[:len(output)-4]
        st.session_state.messages.append({"role": "assistant", "content": output})
    else:
        st.warning("Please process the PDF documents first.")

# Main function
def main():
    st.set_page_config(page_title='Restaurant Recommendation Bot')
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.header('Restaurant Recommendation Bot 🍽️')
    user_question = st.chat_input("Ask a question:")

    if "vectorstore" not in st.session_state:
        data = read_json('combined_file.json')
        docs = json_to_doc(data)
        st.session_state.vectorstore = get_vectorstore(docs)
    
    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})
        handle_userinput(user_question)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

if __name__ == '__main__':
    main()
