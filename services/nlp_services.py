import spacy
from spacy.tokens import Doc


class NLPServices:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nlp = spacy.load("fr_core_news_md")
        return cls._instance

    def analyze_text(self, text: str):
        doc = self.nlp(text)
        return doc

    def clean_text(self, text: str):
        doc: Doc = self.analyze_text(text)
        cleaned_text = ""
        for token in doc:
            if not token.is_stop and token.pos_ not in ["PUNCT", "CCONJ"]:
                cleaned_text += token.lemma_ + " "
        return cleaned_text.strip()
