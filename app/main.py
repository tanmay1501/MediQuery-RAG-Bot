import streamlit as st
from rag import retrieve_answer
from db import init_db

st.set_page_config(page_title="🧬 MedQuAD RAG Chatbot")
st.title("Healthcare Chatbot using pgvector 🧠")

init_db()

query = st.text_input("Ask a medical question:")

if query:
    result = retrieve_answer(query)
    if result:
        st.markdown(f"**Q:** {result[0][0]}")
        st.markdown(f"**A:** {result[0][1]}")
    else:
        st.warning("No relevant answer found.")
