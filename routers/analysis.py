from fastapi import APIRouter
from schemas.analysis import TextRequest
from services.nlp_services import NLPServices

nlp_services = NLPServices()

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

@router.post("/analyze")
async def analyze_text(request: TextRequest):
    doc = nlp_services.analyze_text(request.text)
    tokens = []
    for token in doc:
        tokens.append({
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "shape": token.shape_,
            "is_alpha": token.is_alpha,
            "is_stop": token.is_stop
        })
    return {"tokens": tokens}


@router.post("/clean")
async def clean_text(request: TextRequest):
    cleaned_text = nlp_services.clean_text(request.text)
    return {"cleaned_text: ": cleaned_text}
