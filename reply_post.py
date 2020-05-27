#!/usr/bin/python
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('askreddit')
for submission in subreddit.hot(limit=10):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("belly button", submission.title, re.IGNORECASE):
            try:
                # Reply to the post
                with open("belly_button_facts.txt", "r") as facts:
                        belly_button_facts = []
                        belly_button_facts = facts.read()
                        belly_button_facts = belly_button_facts.split("\n")
                        belly_button_facts = list(filter(None, belly_button_facts))
                        random_fact = belly_button_facts[random.randrange(1, len(belly_button_facts), 1)]
                        submission.reply(random_fact)
                        print("Bot replying to : ", submission.title)

                        # Store the current id into our list
                        posts_replied_to.append(submission.id)
            except praw.exceptions.APIException as e:
                print(submission.author.name)
                print(e)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")