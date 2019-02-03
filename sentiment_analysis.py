
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment as s

#consumer key, consumer secret, access token, access secret.
ckey="3cnJ7zNj2xORpZzf6U5WgrHGK"
csecret="4QNgNsCwKhz3qPoezQIjeNLP6FKHRRsnw1thbpJUgniSAFtBQ9"
atoken="838278439488602112-KZvbB37MsI4RMq4Pr5Z1MOcwRc0H0ed"
asecret="53Q06qktboBhyRgG5fkNhK9YRv0Mz6Ik0iErLlj7CqepO"


class listener(StreamListener):
    
    def on_data(self, data):
        
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        
        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["modi"])
