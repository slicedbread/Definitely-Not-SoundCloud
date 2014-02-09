import json
import urllib2
import requests


class song:
    def __init__(self, name, year, lyrics):
        self.name = name
        self.year = year
        self.lyrics = lyrics

names = [line.strip() for line in open('songs.txt')]

urlpt1="http://musicbrainz.org/ws/2/recording/"
urlpt2 = [line.strip() for line in open('id_file.txt')]
urlpt3="?inc=artist-credits+isrcs+releases&fmt=json"


for i in range(0,3):
	print i, "/500"
	if(urlpt2[i]!="None"):
		url=urlpt1+urlpt2[i]+urlpt3
		#print url
		r = requests.get(url)
		#r.json()
		#print r.json()[1]
		datevar=r.json()['releases'][0]['date'][:4]
		print "bullshit begins: ", datevar