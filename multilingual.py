import nltk
#nltk.download()
from twython import Twython


def bagOfWords(tweets):
    wordsList = []
    for (words, sentiment) in tweets:
      wordsList.extend(words)
    return wordsList

def wordFeatures(wordList):
    wordList = nltk.FreqDist(wordList)
    wordFeatures = wordList.keys()
    return wordFeatures

def getFeatures(doc):
    docWords = set(doc)
    feat = {}
    for word in wordFeatures:
        feat['contains(%s)' % word] = (word in docWords)
    return feat





def read_tweets_a(fname):
    tweets = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        if line.split(',')[-1][:-1]!='obj':
            tweets.append([line.split(',')[0], line.split(',')[-1][:-1]])
        line = f.readline()
    f.close()
    return tweets



Tweets = read_tweets_a('multilingual.txt')




def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        tweets.append([line, t_type])
        line = f.readline()
    f.close()
    return tweets




tweets = []
for (words, sentiment) in Tweets:
    words_filtered = [e.lower() for e in nltk.word_tokenize(words) if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

'''for t in tweets:
    print(t)
'''



def classify_tweet(tweet):
    return \
        classifier.classify(getFeatures(nltk.word_tokenize(tweet)))

    

wordFeatures = wordFeatures(bagOfWords(tweets))

training_set = nltk.classify.apply_features(getFeatures, tweets)
##print training_set
classifier = nltk.NaiveBayesClassifier.train(training_set)

##print(classifier.show_most_informative_features(32))
'''
ConsumerKey = "qatpAvXFxeDxEbmJMUaJAftEq"
ConsumerSecret = "D6ZKDgBzM9nWRNL2gis39zARrItu5IjDTCRWup58U18EoKFSLW"
AccessToken = "1124593926-B2G3ZuplactsnVgZRE2bow2nvdpmg8KtWx66fCu"
AccessTokenSecret = "DJcNsqbFT8gD5uPkYTY0HliXPzF429YLP3FLgfLylzw23"


twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  
queryText = "sometimes i feel i love you"
result = twitter.search(q=queryText)

for status in result["statuses"]:
    print("Tweet: {0} \n Sentiment: {1} \n".format( status["text"].encode('utf-8'), classifier.classify(getFeatures( status["text"].split())).encode('utf-8')))
    #print(nltk.classify.accuracy(classifier, training_set))
# read in the test tweets and check accuracy
# to add your own test tweets, add them in the respective files
'''
test_tweets = read_tweets('dut_test_pos.txt', 'pos')
test_tweets.extend(read_tweets('dut_test_neg.txt', 'neg'))
total = accuracy = float(len(test_tweets))

for tweet in test_tweets:
    print tweet, classify_tweet(tweet[0])
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1

print('Total accuracy: %f%% (%d/20).' % (accuracy / total * 100, accuracy))

print '\n\n\n\n\n\n\n\n\n'

test_tweets = read_tweets('eng_test_pos.txt', 'pos')
test_tweets.extend(read_tweets('eng_test_neg.txt', 'neg'))
total = accuracy = float(len(test_tweets))

for tweet in test_tweets:
    print tweet, classify_tweet(tweet[0])
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1

print('Total accuracy: %f%% (%d/20).' % (accuracy / total * 100, accuracy))

