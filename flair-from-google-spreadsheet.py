import gspread
import AccountDetails
import pickle
import praw
from time import gmtime, strftime

def main():
	gc = gspread.login(AccountDetails.GSPREAD_USERNAME, AccountDetails.GSPREAD_PASSWORD)
	doc = gc.open("Spreadsheet Name").sheet1
	usernames = doc.col_values(2)
	usernames.pop(0) # remove header that just contains the question

	r = praw.Reddit(user_agent='My User Agent 1.0')
	r.login(AccountDetails.REDDIT_USERNAME_BOT, AccountDetails.REDDIT_PASSWORD_BOT)
	
	flairName = 'registered' # choose which flair to apply
	sub = r.get_subreddit('MySubreddit') # and which subreddit to run in

	alreadyAdded = pickle.load(open("flair-form_save.txt", "rb"))

	for user in usernames:
		if user not in alreadyAdded:
			sub.set_flair(user, '', 'registered')
			with open('flair-form_log.txt', 'a') as logfile:
				tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
				lm = ' : ' + flairName + ' @ ' + tn
				logfile.write('\n\rAdded: ' + user + ' : ' + lm)
	        print "Setting flair: " + user + " : " + flairName
	        alreadyAdded.append(user)
	        pickle.dump(alreadyAdded, open("flair-form_save.txt", "wb"))

if __name__ == '__main__':
    main()