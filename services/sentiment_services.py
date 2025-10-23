from transformers import pipeline


class SentimentServices:

    MAX_TEXT_LENGTH: int = 2000
    MAX_LENGTH: int = 512
    SENTIMENT_MODEL: str = "nlptown/bert-base-multilingual-uncased-sentiment"
    STAR_VALUES: dict[str, int] = {
        "1 star": 1,
        "2 stars": 2,
        "3 stars": 3,
        "4 stars": 4,
        "5 stars": 5,
    }

    def __init__(self):
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model=self.SENTIMENT_MODEL,
            tokenizer=self.SENTIMENT_MODEL,
            use_fast=False,
        )

    def truncate_long_text(self, text: str):
        if len(text) >= self.MAX_TEXT_LENGTH:
            text = text[:self.MAX_TEXT_LENGTH]
        return text

    def analyse_sentiment(self, comments: list[str]):
        cleaned_comments = []
        for comment in comments:
            cleaned_text = self.truncate_long_text(comment["text"])
            cleaned_comments.append(cleaned_text)
        result = self.sentiment_pipeline(cleaned_comments, truncation=True, max_length=self.MAX_LENGTH)
        total_sentiment: float = 0
        for r in result:
            total_sentiment += self.STAR_VALUES[r["label"]]
        average_sentiment: float = total_sentiment / len(result)
        return average_sentiment
