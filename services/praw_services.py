import praw
from dotenv import load_dotenv
import os

load_dotenv()

class PrawServices:
    def __init__(self):
        
        self.reddit = praw.Reddit(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            user_agent=os.getenv("USER_AGENT"),
        )

    def get_subreddit(self, subreddit_name: str):
        return self.reddit.subreddit(subreddit_name)

    def test_connection(self):
        """Teste si la connexion fonctionne"""
        print(f"Mode lecture seule : {self.reddit.read_only}")
        print("✅ Connexion réussie !")
    
    def get_comments_from_hot_posts(self, subreddit_name: str = "france", total_comments: int = 300):
        subreddit = self.reddit.subreddit(subreddit_name)
        comments = []
    
        # Parcourt les posts HOT
        for submission in subreddit.hot(limit=30):
            # Charge tous les commentaires du post
            submission.comments.replace_more(limit=0)
            
            # Récupère les commentaires
            for comment in submission.comments.list():
                if len(comments) >= total_comments:
                    break
                    
                comments.append({
                    'text': comment.body,
                    'score': comment.score,
                    'post_title': submission.title,
                    'created_utc': comment.created_utc
                })
            
            if len(comments) >= total_comments:
                break
        
        return comments[:total_comments]
