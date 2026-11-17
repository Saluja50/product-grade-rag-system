
from langchain_openai import ChatOpenAI

from app.config import settings


def get_langchain_llm(feature: str = "rag") -> ChatOpenAI:
    """
    Returns a LangChain ChatOpenAI client connected to LiteLLM.
    """
    return ChatOpenAI(
        api_key=settings.LITELLM_API_KEY,
        base_url=settings.LITELLM_BASE_URL,
        model=settings.LITELLM_MODEL,
        temperature=0,
    )
