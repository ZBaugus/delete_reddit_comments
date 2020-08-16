import praw
import json
import time

#creates a reddit instance using a json config file
def create_reddit_instance():
    with open('reddit_config.json') as f:
        data = json.load(f)

    user_values = data["reddit"]
    reddit = praw.Reddit(client_id = user_values['client_id'], client_secret = user_values['secret_id'], 
    username = user_values['username'], password = user_values['password'], user_agent = user_values['user_agent'])
    return reddit

#Deletes all comments 3 days old or older
def delete_all_comments(r):
    user = r.user.me()
    for c in user.comments.new(limit=100):
        if time.time() - c.created_utc >= 259200.0:
            c.edit('#')
            c.delete()