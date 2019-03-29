#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Sentiment as s
import env
import json

#consumer key, consumer secret, access token, access secret.
ckey=env.API_KEY#"gZyYs6aOfVyPixNIEtme2jQAw"
csecret=env.API_SECRET_KEY#"VFdtnMVeIdueYNbzrSL1YzS5PYq2df37NvykTGys73VbqihJgx"
atoken=env.ACCESS_TOKEN#"832625263208914944-BYhciHVLixagRqwhu8DaxwvQpyfPMOD"
asecret=env.ACCESS_TOKEN_SECRET#"cdMsYnNxzMRPnDvxSBKExaLdLlCL8ilLC4TmAmxVQixbc"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            sentiment_value = s.sentiment(data)
            print(tweet, sentiment_value)
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write("\n")
            output.close()
            return True
            #sentiment_value,confidence = s.sentiment(tweet)
            #print(tweet, sentiment_value, confidence)
            #if confidence*100 >= 80:
            #    output = open("twitter-out.txt", "a")
            #    output.write(sentiment_value)
            #    output.write("\n")
            #    output.close()
            #return True
        except:
            return True   
        def on_error(self, status):
            print (status)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=["#Big4Agenda"])

