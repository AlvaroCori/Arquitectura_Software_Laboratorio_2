import abc
from ls.Artists import Artists
class Audio:
    def __init__(self, name,artist):
        self.__name = name
        self.__artist = artist

    @abc.abstractmethod
    def get_duration(self):
        "recoge la duracion"
    
    @abc.abstractmethod
    def get_number_duration(self):
        "recoge la duracion entera"

    def get_info(self):
        artist_name = ""
        if (self.__artist == None):
            artist_name = "desconocido"
        else:
            artist_name = self.__artist.get_name()
        return f"{self.__name}\n{artist_name}"
    def get_name(self):
        return self.__name
    
    
