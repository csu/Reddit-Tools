import praw
from time import gmtime, strftime
import AccountDetails

def main():
    flairs = {
        'test-flair': 'Test Flair',
    }
    print "Activated: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent='Your User Agent 1.0')
    r.login(AccountDetails.REDDIT_USERNAME_BOT, AccountDetails.REDDIT_PASSWORD_BOT)
    for msg in r.get_unread(limit=None):
        subj = str(msg.subject)
        print "Subject: " + subj
        if subj == 'flair':
            print msg
            auth = str(msg.author)
            body = str(msg.body)
            print "Author: " + auth
            print "Message content: " + body
            sub = r.get_subreddit('SUBREDDIT_HERE')
            if body in flairs:
                ftext = str(flairs[body])
                sub.set_flair(auth, ftext, body)
                with open('log.txt', 'a') as logfile:
                    tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    lm = ' : ' + body + ' @ ' + tn
                    logfile.write('\n\rAdded: ' + auth + ' : ' + ftext + lm)
                print "Setting flair: " + auth + " : " + ftext + " : " + body
                msg.mark_as_read()

if __name__ == '__main__':
    main()