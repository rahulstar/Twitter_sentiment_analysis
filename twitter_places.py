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
			  
result = twitter.get_place_trends(id = 23424977)

if result:
    for trend in result[0].get("trends", []):
        print("{0} \n".format(trend["name"]))
        
