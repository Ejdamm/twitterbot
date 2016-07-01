import tweepy, time, sys, json
from users import Users
 
with open('./twitter_config.json') as config_file:
    conf = json.load(config_file)

auth = tweepy.OAuthHandler(conf["CONSUMER_KEY"], conf["CONSUMER_SECRET"])
auth.set_access_token(conf["ACCESS_KEY"], conf["ACCESS_SECRET"])
api = tweepy.API(auth)

userlist = Users()
while True:
	for user in userlist.users:
		#print user.name
		if True: #user.lastID == 1:
			try:	
				for status in reversed(api.user_timeline(screen_name = user.name, since_id = user.lastID, count = 20, include_rts = False, page = 1)): #change include_rts
					user.lastID = status.id
					#print status.id
					#api.retweet(status.id)
			except tweepy.TweepError as e:
				print user.name
		    		print e.message[0]['code'], e.message[0]['message']
	userlist.writeToFile("users.txt")
	time.sleep(1800) #sleep 30 min
