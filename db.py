import pymongo

class DB:
	
	def __init__(self):
		self.client = pymongo.MongoClient()
		self.db = self.client.database
		self.songs = self.db.songs

	def insert_song(self, song_obj): 
		song_id = self.users.insert(song_obj)
		return song_id

	def list_all(self):
		return self.db.collection_names()
	
	def get_song(self, song_name):
		return self.songs.find_one({"name": song_name})

	def get_all_songs(self):
		return self.songs.find()
