import abc
from Artists import Artists
class Audio:
    def __init__(self, name,artist):
        self.__name = name
        self.__artist = artist

    @abc.abstractmethod
    def get_duration(self):
        "recoge la duracion"

    def get_info(self):
        artist_name = ""
        if (self.__artist == None):
            artist_name = "desconocido"
        else:
            artist_name = self.__artist.getName()
        return f"{self.__name}\n{artist_name}"
    def get_name(self):
        return self.__name
    
    
