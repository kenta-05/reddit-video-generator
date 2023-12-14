import re
import json

reddit_post_data ={'title': '', 'comments': []}

def format_comment(comment: str):
    """Format the comment to remove unnecessary characters"""
    
    _comment = re.sub(r'\[|\]', '', comment) # Remove square brackets
    __comment = re.sub(r'\*', '', _comment) # Remove * marks
    ___comment = re.sub(r'\([^)]*\)', '', __comment) # Remove parentheses and content
    formatted_comment = ___comment
    return formatted_comment

def get_replies(comment: str):
    """Get the replies of the comment recursively"""
    
    replies_list = []
    for reply in comment.replies:
        reply_text = format_comment(reply.body)
        nested_replies_list = get_replies(reply)
        replies_list.append({'comment': reply_text, 'replies': nested_replies_list})
    return replies_list

def save_data(title: str, comments: str):
    """Save the data to a file"""
    
    for comment in comments: # comments is an CommentForest object
        comment_text = format_comment(comment.body) # comment isn't a string, comment_text is a string
        replies_list = get_replies(comment)
        reddit_post_data['comments'].append({'comment': comment_text, 'replies': replies_list})
    reddit_post_data['title'] = title
    json_reddit_post_data = json.dumps(reddit_post_data, indent=2) # convert into JSON
    with open('backend//data/reddit_post_data.json', 'w') as f: # write to file
        f.write(json_reddit_post_data)