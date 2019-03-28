import Sentiment_mod as s
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from http.client import IncompleteRead
import env

#consumer key, consumer secret, access token, access secret.
ckey="gZyYs6aOfVyPixNIEtme2jQAw"
csecret="VFdtnMVeIdueYNbzrSL1YzS5PYq2df37NvykTGys73VbqihJgx"
atoken="832625263208914944-BYhciHVLixagRqwhu8DaxwvQpyfPMOD"
asecret="cdMsYnNxzMRPnDvxSBKExaLdLlCL8ilLC4TmAmxVQixbc"
class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            sentiment_value,confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)
            if confidence*100 >= 80:
                output = open("twitter-out.txt", "a")
                output.write(sentiment_value)
                output.write("\n")
                output.close()
            return True
        except:
            return True
        def on_error(self, status):
            print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener()) twitterStream.filter(track=["Trump"])
