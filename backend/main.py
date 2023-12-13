from app.process.scrape_reddit import scrape_reddit
from app.process.save_data import save_data

# submissionUrl = input('Enter a reddit post url:')
submissionUrl = 'https://www.reddit.com/r/learnprogramming/comments/18dixwu/how_can_i_download_assets_on_oreilly_video/'
title, comments = scrape_reddit(submissionUrl)
save_data(title, comments)
print(title, comments)