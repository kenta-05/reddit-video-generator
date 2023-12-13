import praw
import os
from dotenv import load_dotenv

load_dotenv()

# create read-only reddit instance
reddit = praw.Reddit(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('SECRET_ID'),
    user_agent=os.environ.get('USER_AGENT')
)

submissionUrl = 'https://www.reddit.com/r/learnprogramming/comments/18dwamg/do_you_think_blockchain_development_is_a_good/'

# get submission by url
submission = reddit.submission(url=submissionUrl)
print(submission.title)