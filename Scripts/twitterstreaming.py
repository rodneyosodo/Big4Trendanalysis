import Sentiment as s
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from http.client import IncompleteRead
import env

#consumer key, consumer secret, access token, access secret.
ckey=env.API_KEY
csecret=env.API_SECRET_KEY
atoken= env.ACCESS_TOKEN
asecret=env.ACCESS_TOKEN_SECRET


class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            
            tweet = all_data["text"]
            sentiment_value = s.sentiment(tweet)

            print(tweet, sentiment_value)
            output = open("twitter.txt", "a")
            output.write(str(sentiment_value))
            output.write("\n")
            output.close()  

            return True
        except:
            return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

while True:
    try:
        # Connect/reconnect the stream
        twitterStream = Stream(auth, listener())
        # DON'T run this approach async or you'll just create a ton of streams!
        twitterStream.filter(track=["#big4agenda"])
    except IncompleteRead:
        # Oh well, reconnect and keep trucking
        continue
    except KeyboardInterrupt:
        # Or however you want to exit this loop
        twitterStream.disconnect()
        break