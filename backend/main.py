from app.process.scrape_reddit import scrape_reddit
from app.process.save_data import save_data

# submissionUrl = input('Enter a reddit post url:')
submissionUrl = 'https://www.reddit.com/r/youtube/comments/18jal2k/this_isnt_okay/'

# get title and comments
title, comments = scrape_reddit(submissionUrl)
# save it to file
save_data(title, comments)

