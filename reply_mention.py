#!/usr/bin/python
import praw
import pdb
import re
import os
import random

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we have run the code before, load the list of comments we have replied to
else:
# Read the file into a list and remove any empty values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))
        # Read the list of inbox mentions and check them against comments we have replied to
        for mention in reddit.inbox.mentions(limit=25):
            if mention.id not in comments_replied_to:
                # If we haven't replied to a mention, reply with a random fact pulled from the belly_button_facts.txt file
                try:
                    with open("belly_button_facts.txt", "r") as facts:
                        belly_button_facts = []
                        belly_button_facts = facts.read()
                        belly_button_facts = belly_button_facts.split("\n")
                        belly_button_facts = list(filter(None, belly_button_facts))
                        random_fact = belly_button_facts[random.randrange(1, len(belly_button_facts), 1)]
                        comment = reddit.comment(mention.id)
                        comment.reply(random_fact)
                        comments_replied_to.append(mention.id)
                        print("Replying to comment with fact")
                except praw.exceptions.APIException as e:
                    print(e)
# Add the comments we have replied to the text file we first read from to ensure we don't reply to the same comments
with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")



