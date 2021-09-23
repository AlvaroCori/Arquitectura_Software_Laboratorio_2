
from UnitTest.Audio import Audio
from Audio import Audio

class Album(Audio):

    def __init__(self, name, formatAudio,  artist):
        super(Album, self).__init__(name,formatAudio,artist)
        self.__songs = []
        self.size = 0

    def insertSong(self, song):
        self.__songs.append(song)
        self.size = self.size + 1
        
    def getDuration(self):
        duration = [song.getDuration() for song in self.__song]
        return str(int(duration/60))+":"+str(duration%60)