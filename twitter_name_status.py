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
result = twitter.search(q="sex",count='100',lang="en")
#for status in result["statuses"]:
 #       print(status)
for status in result["statuses"]:
    print("user: {0}\ntext: {1}\ntime: {2}".format(status["user"]["name"].encode('utf-8'),status["text"].encode('utf-8'),status["created_at"]))
    #print (status)
