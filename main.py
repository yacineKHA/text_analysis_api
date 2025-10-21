from fastapi import FastAPI
from routers.analysis import router as analysis_router


app = FastAPI(
    title="Text Analysis API",
    description="""
    API d'analyse de texte en français avec spaCy.
    """
)

app.include_router(analysis_router)