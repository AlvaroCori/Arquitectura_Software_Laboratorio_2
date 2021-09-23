from Audio import Audio
class Song(Audio):
    
    def __init__(self, name, formatAudio,artist,  duration,genre):
        super(Song, self).__init__(name,formatAudio,artist)
        self.__duration = duration
        self.__genre = genre

    def getDuration(self):
        return str(int(self.__duration/60))+":"+str(self.__duration%60)
    def getFichure(self):

        chain = self.__name+"/n"+self.__duration