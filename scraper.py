import praw
import pandas as pd
from datetime import datetime


# Use praw, reddit api to extract info and create a reddit instance
reddit = praw.Reddit(client_id='jp5ihE7tILo0RBfhDHItNQ',
                     client_secret='c7GBj9n01hOzuUEGdsAaK7Tw4ygKzA',
                     user_agent='windows:oxen scraper:v1.0 (by u/Wait_What_Bop)')

# Specify our subreddit
subreddit = reddit.subreddit('nba')

# Get hot posts, we can set limit to be higher if we want more data
hot_posts = subreddit.hot(limit=1000) 

# Create a list to store post dictionaries
post_list = []

# iterate through the posts, and add each post's data to the dataframe
for post in hot_posts:
    post_data = {
        'id': post.id,
        'created_at': datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
        'title': post.title,
        'body': post.selftext,
        'author': post.author.name if post.author else '[deleted]',
        'score': post.ups,
        'url': post.url
    }
    post_list.append(post_data)

df = pd.DataFrame(post_list) #create dataframe from our list
csv_path = "oxennbareddit.csv" 
df.to_csv(csv_path, index=False, encoding='utf-8') #create csv!
