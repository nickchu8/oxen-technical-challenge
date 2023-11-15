import praw
import pandas as pd
from datetime import datetime
import oxen
from oxen.auth import config_auth
from oxen.user import config_user
import os
from oxen.remote_repo import create_repo
from oxen import LocalRepo


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

# #now that we have the csv, let's upload it to oxen
# config_auth("SFMyNTY.g2gDbQAAAC9hcGlfa2V5X3YxOjZhMzc3ZDgwLWIzNDktNGJiMy05MTRjLTJlMWRiYzcyMzExOW4GAB6LNtWLAWIAAVGA.Uv6DnRrz5XM8XNdYXpFXQoymIcrIzBc4omLzFknYCho")
# config_user("Nicholas Chu", "nyc8pv@gmail.com")

# # Create an empty directory named redditchallenge
# directory = "redditchallenge"
# os.makedirs(directory)

# # Initialize the Oxen Repository
# repo = oxen.init(directory)

# # Create a README.md file
# filename = os.path.join(repo.path, "README.md")
# with open(filename, "w") as f:
#     f.write("# Scraping r/nba to get 1000 hot posts")
# # Commit the changes to the repository
# repo.commit("Adding README.md")

# # Create a remote repository
# remote_name = "nickchu8/redditchallenge"
# create_repo(remote_name)

# # Load the local repository
# local_repo = LocalRepo("redditchallenge")

# # Point the local repository to the remote
# local_repo.set_remote(remote_name)

# # Push the changes to the remote repository
# local_repo.push()

# # Add the README.md file to the staging area
# repo.add(filename)
