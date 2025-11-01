"""
Configuration settings for the LangChain chatbot.
"""
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings and configuration."""
    
    # API Keys
    GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # Model Settings
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gemini-2.0-flash-exp")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS: Optional[int] = int(os.getenv("MAX_TOKENS", "2048")) if os.getenv("MAX_TOKENS") else None
    
    # Agent Settings
    MAX_ITERATIONS: int = int(os.getenv("MAX_ITERATIONS", "5"))
    VERBOSE: bool = os.getenv("VERBOSE", "True").lower() == "true"
    
    # Chat History
    MAX_HISTORY_LENGTH: int = int(os.getenv("MAX_HISTORY_LENGTH", "10"))
    
    # File Storage
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "outputs")
    
    # Wikipedia Settings
    WIKI_TOP_K: int = int(os.getenv("WIKI_TOP_K", "2"))
    WIKI_MAX_CHARS: int = int(os.getenv("WIKI_MAX_CHARS", "1000"))
    
    @classmethod
    def validate(cls):
        """Validate required settings."""
        if not cls.GOOGLE_API_KEY and not cls.OPENAI_API_KEY:
            raise ValueError(
                "At least one API key must be set (GOOGLE_API_KEY or OPENAI_API_KEY)"
            )
        return True


# Global settings instance
settings = Settings()
