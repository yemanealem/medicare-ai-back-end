# MediCare AI – Backend

MediCare AI is a FastAPI-based backend system for an **AI-powered medical assistant** designed to improve prescription safety, patient understanding, and healthcare accessibility, particularly in rural and underdeveloped regions.

The system combines **Retrieval-Augmented Generation (RAG)**, verified clinical data, and **localized AI responses** to reduce hallucinations and help both doctors and patients verify prescriptions before medication is taken.

---

## 🚀 Key Features

* Secure authentication using JWT
* AI-powered medical chat with conversation history
* Prescription validation using verified clinical drug data
* Retrieval-Augmented Generation (RAG) to reduce AI hallucinations
* Localized, patient-friendly medical explanations
* Persistent storage of users, messages, and clinical data
* Scalable architecture suitable for SaaS or EMR integration

---

## 🏗️ Tech Stack

* **Backend Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Database:** PostgreSQL (production), SQLite (development)
* **AI Orchestration:** LangChain
* **LLM:** Google Gemini 2.0
* **Vector Store:** ChromaDB
* **Embeddings:** Google Generative AI Embeddings

🧠 AI & RAG Overview

MediCare AI uses Retrieval-Augmented Generation (RAG) to ensure safe and grounded medical responses:

Drug information is stored in a local PostgreSQL database

Data is embedded using Google Generative AI embeddings

Embeddings are stored in ChromaDB

Relevant clinical context is retrieved per query

The LLM generates responses grounded in verified data

This approach significantly reduces hallucinations and improves the reliability of medical guidance.


🌍 Localization & Patient Safety

The system supports localized medical information, allowing responses to be generated in patient-friendly language. This improves understanding, treatment adherence, and reduces medication misuse, especially in multilingual and low-literacy environments.



