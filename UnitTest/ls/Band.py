from ls.Artists import Artists
class Band(Artists):
    def __init__(self, artist, popularity) :
        Artists.__init__(self,artist["name"],artist["experience"],artist["followers"])
        self.__popularity = popularity
        self.__artists = []
    def insert_artist(self, artist):
        self.__artists.append(artist)
    def get_info(self):
        artists = ""
        for artist in self.__artists:
            artists += f"\n* {artist.get_name()}"
        return f"{super().get_info()}\n{self.__popularity*100}%{artists}"
    
