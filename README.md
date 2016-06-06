Extracting tweets from twitter using twython and classifying the tweets as positive and negative using python module NLTK
The projects aims at extracting the live tweets from twitter using OAUth https://dev.twitter.com/oauth which is wrapper class for twitter API 

further the projects classifies those tweets as positive tweets or negative tweets using the training data(happy.txt and sad.txt containing positive and negative tweets respectively), and NLTK module 

Finally the accuracy of the tweets are tested using a test file happy_test.txt and sad_test.text and the accuracy is found to be 90.80% 
these files contains the pre classified data and are mapped with new classified data given by NLTK

the sentiment analysis was made on different language dataset (german and dutch ) and review of various products were collected using the live tweet by varying the query text(
Überprüfung der Galaxie s7) for getting the review of gakaxy s7 in german and analysis abt popularity of various product can be made easily;

the review for test product were further analysed and found to be around 88% accuraccy in german and 81 %accuracy in dutch

the sentiment analysis was again made on new multilingual data set  and efficiency was found to be low as compared to dutch , eng,germany but however in case of multilingual slangs and text present in the tweets the multilingual classification holds a good result;the efficiency is low bcz 1/2 of the data set remains unsed if the text in the tweets are of single language;

prerequisites 

NLTK http://www.nltk.org/data.html

TWYTHON https://pypi.python.org/pypi/twython 

python 2.7 https://www.python.org/download/releases/2.7/
