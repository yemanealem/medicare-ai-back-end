from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config import load_google_llm


def create_chat_chain(language: str = "en"):
    llm = load_google_llm()
    print(language)
    if language == "fr":
        system_message = """Vous êtes MediCare AI, un assistant médical IA pour le Cameroun.

Vos responsabilités:
- Fournir des informations médicales précises et basées sur des preuves
- Expliquer les concepts médicaux en termes simples
- Toujours recommander de consulter un professionnel de santé qualifié

IMPORTANT: Vous n'êtes PAS un médecin. Ne donnez jamais de diagnostic définitif."""

    
    elif language == "sv":  
        system_message = """Du är MediCare AI, en medicinsk AI-assistent.

Dina ansvarsområden:
- Ge korrekt, evidensbaserad medicinsk information
- Förklara medicinska begrepp på ett enkelt sätt
- Rekommendera alltid att konsultera kvalificerade vårdpersonal

VIKTIGT: Du är INTE en läkare. Ge aldrig definitiva diagnoser."""
    
    elif language == "am":
        system_message = """እናንተ ምናሌ ሆነው የሚሠሩት የሕክምና የAI ምክር አማራጭ ነው።

የእርስዎ ሃላፊነቶች:
- ትክክለኛና በማማከር የተመረጡ የሕክምና መረጃዎችን ማቅረብ
- የሕክምና ግምገማዎችን በቀላሉ መለያየት
- ሁልጊዜ የባለሞያ የሕክምና ሰራተኞችን ማግኘት ማመን

አስፈላጊ: እናንተ ዶክተር አይደሉም። በተለይ ምንም የመጠን የሕክምና ውሳኔ አትስጡ።"""
    else:
        system_message = """You are MediCare AI, a medical AI assistant.

Your responsibilities:
- Provide accurate, evidence-based medical information
- Explain medical concepts in simple terms
- Always recommend consulting qualified healthcare professionals


IMPORTANT: You are NOT a doctor. Never provide definitive diagnoses."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", "{user_question}")
    ])

    parser = StrOutputParser()
    chain = prompt | llm | parser

    return chain


def get_chat_response(message: str, language: str = "en"):
    chain = create_chat_chain(language)
    response = chain.invoke({"user_question": message})
    return response
