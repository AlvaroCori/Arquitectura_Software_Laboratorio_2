
from Audio import Audio
class Album(Audio):

    def __init__(self, audio):
        Audio.__init__(self, audio["name"],audio["artist"])
        self.__songs = []
        self.size = 0

    def insert_song(self, song):
        self.__songs.append(song)
        self.size = self.size + 1
        
    def get_duration(self):
        duration = []
        if (self.size > 0):
            duration = [song.get_name()+" = "+song.get_duration() for song in self.__songs]
        return duration

    def get_info(self):
        return f"canciones del album: {self.size}\n{super().get_info()}"
    
    def get_number_duration(self):
        duration = 0
        for song in self.__songs:
            duration += song.get_number_duration()
        return duration