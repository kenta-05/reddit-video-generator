import praw
import os
from dotenv import load_dotenv
load_dotenv()

def scrape_reddit(submissionUrl: str, limit: int = 0):
    # create read-only reddit instance
    reddit = praw.Reddit(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('SECRET_ID'),
        user_agent=os.environ.get('USER_AGENT')
    )

    # attributes of submission -> https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
    submission = reddit.submission(url=submissionUrl)
    title = submission.title
    comments = submission.comments

    return title, comments
