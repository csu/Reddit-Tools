import praw
import os
import json
import AccountDetails

def main():
    r = praw.Reddit(user_agent='My User Agent 1.0')
    r.login(AccountDetails.REDDIT_USERNAME, AccountDetails.REDDIT_PASSWORD)
    sub = r.get_subreddit(INSERT YOUR SUBREDDIT NAME HERE)
    save = []
    for flair in sub.get_flair_list(limit=None):
    	save.append(flair)
    with open(os.path.join(dir, 'flair-save.json'), 'w') as outfile:
        json.dump(save, outfile)
    sub.clear_all_flair()

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    main()