import tweepy
import csv

#Twitter API credentials
consumer_key = "Touoy11VbEO0pyBKcfcfHPGbX"
consumer_secret = "M9NK8xEodEP1JWEluyHdVpMEfdaLaMNpZfhh8PDlPZVxgTh8tS"
access_key = "961266334393913344-RKxLLdStU8YeR3pancZaSOYaHFNokJQ"
access_secret = "Wmrr7naVx30m6ue73iQ1EIOgQXpWH0NP47M1CY0HFiNWD"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	

	outtweets = [[tweet.created_at,tweet.place,tweet.text.encode("utf-8"),tweet.lang] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["created_at","place","text","lang"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("BarackObama")
