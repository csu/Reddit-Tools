import praw
import AccountDetails

def main():
    r = praw.Reddit(user_agent='My First Bot 1.0')
    r.login(AccountDetails.REDDIT_USERNAME, AccountDetails.REDDIT_PASSWORD)
    totalLinkKarma = 0
    totalCommentKarma = 0
    numOfAccounts = 0
    # reddit_usernames should be a list of usernames in AccountDetails
    for username in AccountDetails.reddit_usernames:
        try:
            user = r.get_redditor(username)
            userLinkKarma = user.link_karma
            userCommentKarma = user.comment_karma
            if (userLinkKarma != 1) and (userCommentKarma != 0):
                totalLinkKarma += userLinkKarma
                totalCommentKarma += userCommentKarma
            numOfAccounts += 1
            print "---------------"
            print username + ": (" + str(userLinkKarma) + "|" + str(userCommentKarma) + ")"
        except:
            print "Failed to fetch karma for " + username
    print "Num. of accounts: %d | Total link karma: %d | Total comment karma: %d" % (numOfAccounts, totalLinkKarma, totalCommentKarma)

if __name__ == '__main__':
    main()