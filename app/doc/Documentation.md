## MediCare AI Backend Documentation

Overview

MediCare AI Backend is a FastAPI-based backend system designed to support an AI-powered medical assistant. The system focuses on patient safety, prescription understanding, and localized medical guidance. It provides secure authentication, persistent medical chat history, and integration with Retrieval-Augmented Generation (RAG) to reduce hallucinations by grounding AI responses in verified clinical data.

The backend is built using FastAPI, SQLAlchemy, PostgreSQL/SQLite, LangChain, ChromaDB, and Google Generative AI (Gemini 2.0).

Key features include:

Secure patient authentication with JWT-based authorization

AI-powered medical chat with conversation tracking

Prescription-related medical guidance backed by verified data

Retrieval-Augmented Generation (RAG) to reduce AI hallucinations

Persistent storage of user conversations and metadata

Modular, scalable architecture suitable for SaaS or EMR integration

1. System Architecture (High Level)

The backend follows a layered architecture:

# API Layer (FastAPI): Exposes RESTful endpoints for authentication, chat, and data access

# Service Layer: Contains business logic, AI orchestration, and validation rules

# AI Layer (LangChain + RAG): Handles prompt orchestration, retrieval, and LLM interaction

# Data Layer: PostgreSQL/SQLite for structured data and ChromaDB for vector storage

The system is designed to allow both doctors and patients to verify and understand medical prescriptions using AI while ensuring data privacy and regulatory compliance.

2. Technology Stack

Backend Framework: FastAPI

ORM: SQLAlchemy

Database: PostgreSQL (production), SQLite (development/testing)

Authentication: JWT (JSON Web Tokens)

AI Orchestration: LangChain

LLM: Google Gemini 2.0

Vector Database: ChromaDB

Embeddings: Google Generative AI Embeddings
