class Song:
    def __init__(self, duration,genre):
        self.__duration = duration
        self.__genre = genre
    def getDuration(self):
        return str(int(self.__duration/60))+":"+str(self.__duration%60)