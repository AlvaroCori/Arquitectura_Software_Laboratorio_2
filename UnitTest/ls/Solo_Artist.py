from ls.Artists import Artists
class Solo_Artist(Artists):
    def __init__(self, artist, birthday) :
        Artists.__init__(self,artist["name"],artist["experience"],artist["followers"])
        self.__birtday = birthday
    def get_info(self):
        return f"{super().get_info()}\n{self.__birtday[0]}/{self.__birtday[1]}/{self.__birtday[2]}"