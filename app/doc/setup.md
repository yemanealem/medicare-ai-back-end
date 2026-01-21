Prerequisites

Ensure the following tools are installed on your system:

Python: >= 3.10

pip or pipx

Virtualenv (optional but recommended)

PostgreSQL: >= 14

Git

Setup Instructions

1. Clone the Repository
   git clone https://github.com/yemanealem/medicare-ai-back-end.git
   cd your-fastapi-backend

2. Create and Activate a Virtual Environment
   python -m venv venv

Activate the environment:

Linux / macOS

source venv/bin/activate

Windows

venv\Scripts\activate

activate pip install -r requirements.txt
uvicorn app.main:app --reload

# ===============================

# Server Configuration

# ===============================

PORT=8000
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# ===============================

# AI / LLM Configuration

# ===============================

GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=gemini-2.0-flash-exp
TEMPERATURE=0.7
MAX_TOKENS=2048

# ===============================

# Web Search / RAG

# ===============================

TAVILY_API_KEY=your_tavily_api_key

# ===============================

# Database Configuration

# ===============================

DATABASE_URL=postgresql://meduser:admin@localhost:5432/med_db
