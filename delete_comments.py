import praw
import reddit_methods

reddit = reddit_methods.create_reddit_instance()
user = reddit.user.me()
reddit_methods.delete_all_comments(reddit)
