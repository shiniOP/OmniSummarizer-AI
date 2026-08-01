import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0.3,#->  0.2–0.3 for Summarization
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )