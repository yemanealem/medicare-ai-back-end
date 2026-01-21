from fastapi import FastAPI, Depends, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import settings
from app.routes import health, analysis, research, auth,prescription,drug
from app.database import Base, engine, SessionLocal, get_db
from app.models.user import User
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.middleware.logger_middleware import LoggingMiddleware
from app.logger import logger


Base.metadata.create_all(bind=engine)
bearer_scheme = HTTPBearer()

app = FastAPI(
    title="MediCare AI Backend",
    description="Medical AI Assistant API for Patients - Powered by LangChain and Retrieval-Augmented Generation (RAG)",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Middleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.add_middleware(LoggingMiddleware)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "path": request.url.path
        }
    )



# Include routers
app.include_router(health.router)
app.include_router(analysis.router)
app.include_router(research.router)
app.include_router(auth.router)
app.include_router(prescription.router)
app.include_router(drug.router)


# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to MediCare AI Backend",
        "version": "2.0.0",
        "powered_by": "LangChain +RAG + Google Gemini",
        "docs": "/docs",
        "status": "running"
    }

# Example protected route using raw JWT
@app.get("/me")
async def get_me(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    """
    This route accepts a raw JWT token in Swagger "Authorize".
    Click "Authorize" and paste your token as `Bearer <your_token>`.
    """
    token = credentials.credentials
    return {"token_received": token}
