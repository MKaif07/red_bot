import praw
import reader
import red_cred as rc

reddit = praw.Reddit(
    client_id=rc.creds['client_id'],
    client_secret=rc.creds['client_secret'],
    username=rc.creds['username'],
    password=rc.creds['password'],
    user_agent=rc.creds['user_agent'],
)

def sub_read():
    subs=[]
    subs = reader.reading_file()
    return subs

def get_latest(subs :list):
    if subs is None:
        return
    for sub in subs:
        print("\nSubreddit: {} \n".format(sub))
        subreddit = reddit.subreddit(str(sub))
        latest_sub = subreddit.new(limit=10)
        for submission in latest_sub:
            print("Title: {} \n Score: {} \n Url: {}"
                  .format(submission.title, submission.score, submission.url))
            print(20*'-')
            
def get_hot(subs :list):
    if subs is None:
        return
    for sub in subs:
        print("\nSubreddit: {} \n".format(sub))
        subreddit = reddit.subreddit(str(sub))
        hot_sub = subreddit.hot(limit=10)
        for submission in hot_sub:
            print("Title: {} \n Score: {} \n Url: {}"
                  .format(submission.title, submission.score, submission.url))
            print(20*'-')

def get_controversial(subs :list):
    if subs is None:
        return
    for sub in subs:
        print("\nSubreddit: {} \n".format(sub))
        subreddit = reddit.subreddit(str(sub))
        cont_sub = subreddit.controversial(time_filter="week")
        for submission in cont_sub:
            print("Title: {} \n Score: {} \n Url: {}"
                  .format(submission.title, submission.score, submission.url))
            print(20*'-')

def menu():
    print("1. get latest posts from subs in list")
    print("2. get hot posts from subs in list")
    print("3. get controversial posts froms subs")

    ch = int(input("Enter Choice: "))
    if ch == 1:
        get_latest(sub_read())
    elif ch == 2:
        get_hot(sub_read())
    elif ch == 3:
        get_controversial(sub_read())
    else:
        print("Enter a valid Choice")
        menu()
    return
        

if __name__ == '__main__':
    
    menu()
    print(40*'#')
