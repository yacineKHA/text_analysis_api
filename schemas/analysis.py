from pydantic import BaseModel, Field
from typing import List, Optional

class TextRequest(BaseModel):
    text: str = Field(..., min_length=2, description="Texte à analyser")


class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int


class AnalysisResponse(BaseModel):
    """Réponse de l'analyse"""
    text: str
    language: str
    sentiment: str
    sentiment_score: float
    keywords: List[str]
    entities: List[Entity]
    summary: Optional[str] = None
    word_count: int
    sentence_count: int