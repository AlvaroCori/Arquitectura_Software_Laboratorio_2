import abc
from Artists import Artists
class Audio:
    def __init__(self, name,formatAudio,artist):
        self.__name = name
        self.__format = formatAudio
        self.__artist = artist

    @abc.abstractmethod
    def getDuration(self):
        "recoge la duracion"

    def getAudioInfo(self):
        return f"{self.__name}\n{self.__format}\n{self.__artist.getName()}"
    
