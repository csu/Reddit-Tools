#!/usr/bin/python
import praw
import sys
import AccountDetails

def main():
	r = praw.Reddit(user_agent='My User Agent 1.0')
	r.login(AccountDetails.REDDIT_USERNAME, AccountDetails.REDDIT_PASSWORD)
	r.submit('MySubreddit', sys.argv[1], url=sys.argv[2])

if __name__ == '__main__':
    main()