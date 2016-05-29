#import twython
from twython import Twython

ConsumerKey = "qatpAvXFxeDxEbmJMUaJAftEq"
ConsumerSecret = "D6ZKDgBzM9nWRNL2gis39zARrItu5IjDTCRWup58U18EoKFSLW"
AccessToken = "1124593926-B2G3ZuplactsnVgZRE2bow2nvdpmg8KtWx66fCu"
AccessTokenSecret = "DJcNsqbFT8gD5uPkYTY0HliXPzF429YLP3FLgfLylzw23"



twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  
				  
time = twitter.get_user_timeline(screen_name = "stanfordeng", count = 5)
for tweet in time:
    print(" User: {0} \n Created: {1} \n Text: {2} "
          .format(tweet["user"]["name"],
                  tweet["created_at"],
                  tweet["text"]))
