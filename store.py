import pylast
import config

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm
API_KEY =  config.key # this is a sample key
API_SECRET = config.secret 

# In order to perform a write operation you need to authenticate yourself
username = config.user 
password_hash = pylast.md5(config.pw)

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET, username = username, password_hash = password_hash)

f = open ('songs.txt', 'r')

for item in f:
	splits = item.split('--')[1].split('-')
	track = network.get_track(splits[1], splits[2])

track = network.get_track("Iron Maiden", "The Nomad")

f.close()
p.close()

# type help(pylast.LastFMNetwork) or help(pylast) in a python interpreter to get more help
# about anything and see examples of how it works
