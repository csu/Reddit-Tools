import praw, time, pickle, webbrowser
from time import gmtime, strftime
import AccountDetails

sub_storage = []

def main():
    global r
    global sub_storage

    print "Activated: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    userInput = raw_input("Would you like to [s]crape, [c]omment, or [d]elete? ")
    if userInput == 'c' or userInput == 'comment':
        r = praw.Reddit(user_agent='My User Agent 1.0')
        r.login(AccountDetails.REDDIT_USERNAME, AccountDetails.REDDIT_PASSWORD)
        sub_storage = pickle.load(open("quick_comment_saved.txt", "rb"))
        comment()
    elif userInput == 'd' or userInput == 'delete':
        delete_sub_storage()
    else:
        r = praw.Reddit(user_agent='My User Agent 1.0')
        r.login(AccountDetails.REDDIT_USERNAME, AccountDetails.REDDIT_PASSWORD)
        sub_storage = pickle.load(open("quick_comment_saved.txt", "rb"))
        scrape()

def delete_sub_storage():
    sub_storage = []
    pickle.dump(sub_storage, open("quick_comment_saved.txt", "wb"))

def scrape():
    global sub_storage
    ignoreWords = ['women of reddit', 'doctors of reddit', 'teachers of reddit']

    while True:
        subreddit = r.get_subreddit('AskReddit')
        for submission in subreddit.get_new(limit=10):
            op_text = submission.selftext.lower()
            does_not_have_ignore = not any(string in op_text for string in ignoreWords)
            if submission.id not in sub_storage and does_not_have_ignore:
                print "Storing: " + submission.id
                sub_storage.append(submission.id)
        print "Pickleing. " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
        pickle.dump(sub_storage, open("quick_comment_saved.txt", "wb"))
        time.sleep(150)

def comment():
    global sub_storage
    for sub_id in sub_storage:
        submission = r.get_submission(submission_id = sub_id)
        if submission.title.count(' ') < 3: # remove spam posts that get scraped before mods remove them
            sub_storage.remove(sub_id)
        else:
            print "\n------------------\n" + submission.title + "\n---\n" + submission.selftext
            userInput = raw_input("Enter comment [o,e]: ")
            if userInput == '':
                sub_storage.remove(sub_id)
            elif userInput == 'exit' or userInput == 'e':
                pickle.dump(sub_storage, open("quick_comment_saved.txt", "wb"))
                break
            elif userInput == 'open' or userInput == 'o':
                webbrowser.open(submission.permalink)
                sub_storage.remove(sub_id)
            else:
                submission.add_comment(userInput)
                sub_storage.remove(sub_id)
    pickle.dump(sub_storage, open("quick_comment_saved.txt", "wb"))

if __name__ == '__main__':
    main()