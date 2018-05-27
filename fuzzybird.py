#!/usr/bin/env python3

import sys
import twitter
import soundex
import unicodedata
import config
import tweetgui

def get_hashtag_tweet(hashtag, count):
    results = api.GetSearch(raw_query="l=&q=%23" + hashtag + "&count=" + str(count))
    results = [result.text for result in results]
    results = [r.replace('\n', ' ').replace('\r', '') for r in results]
    return results

if __name__ == "__main__":
    args = config.arg_logic()
    keys = config.parse_config(args.config_file)

    api = twitter.Api(
            consumer_key        = keys['consumerkey'],
            consumer_secret     = keys['consumersecret'],
            access_token_key    = keys['accesstokenkey'],
            access_token_secret = keys['accesstokensecret']
            )

    if not args.hashtag:
        args.hashtag = input("Enter your hashtag: ")

    hashtags = [unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode('ascii') for text in get_hashtag_tweet(args.hashtag, 1000)]
    encoded_hashtags = soundex.encode_phrases(hashtags)
    tweetgui.execute(hashtags, encoded_hashtags)
