import sys
import twitter
import soundex
import unicodedata

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')


def get_hashtag_tweet(hashtag, count):
    results = api.GetSearch(raw_query="l=&q=%23" + hashtag + "&count=" + str(count))
    return [result.text for result in results]


sys.stdout.write('Enter a hashtag: ')
hashtag = raw_input()
hashtags = [unicodedata.normalize('NFKD', text).encode('ascii','ignore') for text in get_hashtag_tweet(hashtag, 1000)]
print("RESULTS:", len(hashtags))
encoded_hashtags = soundex.encode_phrases(hashtags)

while True:
    user_input = raw_input()
    if user_input.strip() == "": # empty line signals stop
        break
    for match in soundex.match(user_input, hashtags, encoded_hashtags):
        print match
