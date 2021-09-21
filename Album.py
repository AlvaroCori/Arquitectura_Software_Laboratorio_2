class Album:
    def __init__(self):
        self.__songs = []
        self.size = 0

    def insertSong(self, song):
        self.__songs.append(song)
        self.size = self.size + 1
        
    def getDuration(self):
        duration = [song.getDuration() for song in self.__song]
        return str(int(duration/60))+":"+str(duration%60)