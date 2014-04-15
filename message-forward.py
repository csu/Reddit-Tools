'''
message-forward.py
Christopher Su
http://christophersu.net/
Forwards unread messages from one Reddit account to another.
'''

import praw
import AccountDetails

def main():
	r = praw.Reddit(user_agent='My User Agent 1.0')
	r.login(AccountDetails.REDDIT_USERNAME_RECEIVER, AccountDetails.REDDIT_PASSWORD_RECEIVER)
	for msg in r.get_unread(limit=None):
		r.send_message(AccountDetails.REDDIT_USERNAME_FORWARD_TO, "Fwd: " + msg.subject, "From: %s\n\n> %s" % (str(msg.author), msg.body))

if __name__ == '__main__':
	main()