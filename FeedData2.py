import db
import re


class song:
    def __init__(self, name, year, lyrics):
        self.name = name
        self.year = year
        self.lyrics = lyrics




#songs = [line.strip() for line in open('songs.txt')]

years = [0]*500
x = 0
f = open('years.txt', 'r')
for line in f:
	years[x]=line.split()[1]
	x+=1

songsTooTired = [0]*500
songs = [0]*500
xx = 0
ff = open('songs.txt', 'r')
for line in ff:
	songsTooTired[xx]=line
	songs[xx]=line.split("--")[1]
	xx+=1


xxx = 0;
for songName in songsTooTired:
	songNameSHIT="./Data/"+songName[:-1]+" .txt"
	lyricFiles=open(songNameSHIT, "r").readlines()
	
	buff=[]
	#print "asdflyricFiles: ", lyricFiles
	for lyr in lyricFiles:
		#print "lyr: ",lyr
		#print "lyricFiles: ", lyricFiles
		buff.append(re.findall(r'\w+', lyr))
	#print buff
	print songs[xxx]
	db.insert_song(songs[xxx],"",years[xxx],buff)
	xxx+=1








	