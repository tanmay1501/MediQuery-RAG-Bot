# 🏥 MedQuery-RAG-Bot: Healthcare Semantic Search Chatbot with Streamlit, LangChain, LLM, and pgvector

---

## 📄 Project Overview

**MedQuad-RAG** is a full-stack **Retrieval-Augmented Generation (RAG)** system designed to provide semantically accurate, real-world answers to healthcare-related queries by retrieving context from the **MedQuad dataset**.

Built using:
- **Streamlit** for the user-facing Chatbot interface
- **LangChain** to orchestrate retrieval and LLM calls
- **Azure OpenAI / OpenAI** GPT models for response generation
- **PostgreSQL + pgvector** for high-performance vector-based retrieval
- **Docker Compose** for easy orchestration and deployment

---

## 🚀 Features

- 🔍 Semantic search over the MedQuad healthcare QA dataset
- 🧠 RAG Pipeline: Retrieve relevant documents + generate contextualized answers
- 🐅️ Vector storage using PostgreSQL + pgvector
- 💽 Interactive chatbot UI built with Streamlit
- ⚙️ Containerized with Docker for local and cloud deployment
- 📚 Scalable to millions of documents and real LLMs (e.g., Azure OpenAI GPT-4)

---

## 🏗️ Architecture Diagram

```
User (Streamlit chatbot)
    ↓
LangChain (Retriever + LLM Chain)
    ↓
pgvector (Semantic Retriever)
    ↔
PostgreSQL (Embedded MedQuad chunks)
    ↔
LLM (Azure OpenAI GPT-4 / OpenAI GPT-3.5)
```

---

## 📆 Tech Stack

| Component        | Technology                     |
|------------------|---------------------------------|
| UI               | Streamlit |
| Framework        | LangChain |
| LLM              | Azure OpenAI GPT-4 / GPT-3.5 |
| Embedding Model  | OpenAI Ada-002 (or local sentence-transformer) |
| Vector Database  | PostgreSQL + pgvector |
| Deployment       | Docker Compose |

---

## 📚 Dataset

- **MedQuad**: Medical Questions and Answers sourced from NIH, PubMed, MedlinePlus.
- Preprocessed, chunked, embedded, and stored for fast retrieval.

---

## 🛠️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medquad-rag.git
cd medquad-rag
```

---

### 2. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-or-azure-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4
POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
POSTGRES_DB=semanticdb
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

### 3. Build and Run Services

```bash
docker-compose up --build
```

This will:
- Start **PostgreSQL + pgvector** database
- Start **FastAPI** backend (optional if used for advanced RAG)
- Start **Streamlit chatbot frontend**

---

### 4. Populate the Database (Optional)

Load MedQuad embeddings:

```bash
python backend/load_medquad_embeddings.py
```

---

### 5. Access the Application

- Streamlit Chatbot → [http://localhost:8501](http://localhost:8501)

Start asking medical or healthcare-related questions to the RAG model!

---

## 🐳 Docker Setup

| Service | Description |
|---------|-------------|
| db      | PostgreSQL with pgvector |
| api     | FastAPI or LangChain server (optional for large systems) |
| frontend | Streamlit app |

---

## 📌 Key Components

| Component | Description |
|-----------|-------------|
| Retriever | pgvector via LangChain’s `VectorStoreRetriever` |
| Embeddings | OpenAI Ada-002 or custom embeddings |
| RAG Chain | LangChain RetrievalQA chain |
| LLM | Azure OpenAI GPT or OpenAI API |

---

## 🔒 Security Considerations

- No external data sharing with OpenAI unless explicitly configured
- API keys managed securely via environment variables
- Future: Add authentication for enterprise usage

---

## 📈 Future Improvements

- 🔄 Re-ranking retrieved results with LLM scoring
- 🧠 Multi-turn conversational memory
- 📝 Dynamic document ingestion through admin portal
- 📊 Usage analytics dashboard
- 🛡️ OAuth2-based user authentication for enterprise access

---

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.dev/)
- [Sentence Transformers](https://www.sbert.net/)
- [OpenAI](https://openai.com/)
- [MedQuad Dataset](https://github.com/abachaa/MedQuAD)
- [pgvector](https://github.com/pgvector/pgvector)

---

# 🚀 Let's bring healthcare search into the AI era!

