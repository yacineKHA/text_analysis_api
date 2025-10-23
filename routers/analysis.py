from fastapi import APIRouter
from schemas.analysis import TextRequest
from services import praw_services
from services.nlp_services import NLPServices
from services.praw_services import PrawServices
from sklearn.feature_extraction.text import TfidfVectorizer
from services.sentiment_services import SentimentServices

nlp_services = NLPServices()
praw_services = PrawServices()
sentiment_services = SentimentServices()

router = APIRouter(prefix="/api", tags=["api"])


@router.post("/analyze")
async def analyze_text(request: TextRequest):
    doc = nlp_services.analyze_text(request.text)
    tokens = []
    for token in doc:
        tokens.append(
            {
                "text": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_,
                "tag": token.tag_,
                "dep": token.dep_,
                "shape": token.shape_,
                "is_alpha": token.is_alpha,
                "is_stop": token.is_stop,
            }
        )
    return {"tokens": tokens}


@router.post("/clean")
async def clean_text(request: TextRequest):
    cleaned_text = nlp_services.clean_text(request.text)
    return {"cleaned_text: ": cleaned_text}


@router.get("/test_praw")
async def test_praw():
    try:
        praw_services.test_connection()
    except Exception as e:
        return {"message": str(e)}


@router.get("/get_comments")
async def get_com():
    try:
        comments = praw_services.get_comments_from_hot_posts()
        return {"comments": comments}
    except Exception as e:
        return {"message": str(e)}


@router.get("/get_sentiment")
def get_sentiment():
    try:
        comments = praw_services.get_comments_from_hot_posts()
        result = sentiment_services.analyse_sentiment(comments)
        return {"result: ": result}
    except Exception as e:
        return {"message": str(e)}


@router.get("/get_tfidf")
async def get_tfidf():
    try:
        comments = praw_services.get_comments_from_hot_posts()
        cleaned_comments = []
        for comment in comments:
            cleaned_comments.append(nlp_services.clean_text(comment["text"]))
        vectorizer = TfidfVectorizer(max_features=30)
        vectorizer.fit_transform(cleaned_comments)
        keywords = vectorizer.get_feature_names_out()
        return {"keywords: ": list(keywords)}
    except Exception as e:
        return {"message": str(e)}
