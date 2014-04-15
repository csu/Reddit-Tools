import praw
import urllib2
from time import gmtime, strftime
import AccountDetails

# main function
def main():
    flairSet = { # format: flair-title:Flair Text
        'registered': '',
    }

    print "Activated: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent='My User Agent 1.0') # user agent
    r.login(AccountDetails.REDDIT_USERNAME_BOT, AccountDetails.REDDIT_PASSWORD_BOT) # login to reddit

    flairName = 'registered' # choose which flair to apply
    sub = r.get_subreddit('Subreddit') # and which subreddit to run in

    file = urllib2.urlopen('URL TO TEXT FILE')
    userSet = set(line.strip() for line in file)
    # print userSet
    
    for userToFlair in userSet:
        if flairName in flairSet:
            flairText = str(flairSet[flairName])
            sub.set_flair(userToFlair, flairText, flairName)
            with open('log.txt', 'a') as logfile:
                tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                lm = ' : ' + flairName + ' @ ' + tn
                logfile.write('\n\rAdded: ' + userToFlair + ' : ' + flairText + lm)
            print "Setting flair: " + userToFlair + " : " + flairText + " : " + flairName

if __name__ == '__main__':
    main()