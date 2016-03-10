from twython import Twython
import pprint
import json

TWITTER_APP_KEY = 'wFJqerYMWc6soLWKdkoexOZEi'
TWITTER_APP_KEY_SECRET = '7irYpfIcQyFqrUZiHMJ7Vfgoj40aIQZqHydkF3LpUdr6juKsY0'
TWITTER_ACCESS_TOKEN = '3595841234-oOs2afeCb9kkz3fzgCi3XGtQdGRbl5wWEiLoZGi'
TWITTER_ACCESS_TOKEN_SECRET = 'W7tS0P7gphK3HzHjQmASuGdMTntvZNlJPYozwERTaKWpo'

t = Twython(app_key=TWITTER_APP_KEY,app_secret=TWITTER_APP_KEY_SECRET ,oauth_token=TWITTER_ACCESS_TOKEN, oauth_token_secret = TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q = 'amazon iphone6', count = 1000, language = 'eng')

tweets = search['statuses']



a = dict()
i=0
for tweet in tweets:
    print tweet['text'], "\n"
    a[i] = tweet['text']
    i=i+1
fil=open('amazon.json','w')
json.dump(a, fil)   
    
